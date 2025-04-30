from django import forms
from django.contrib.auth import get_user_model
from build_people.models import CoreValue, Recognition
from users.enums import RecognitionPoints

User = get_user_model()

class CreateRecognitionForm(forms.ModelForm):
    points = forms.ChoiceField(choices=RecognitionPoints, required=True, initial=RecognitionPoints.TEN)

    class Meta:
        model = Recognition
        fields = ["receiver", "points", "core_values", "message"]

    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user", None)
        super().__init__(*args, **kwargs)

        self.fields["receiver"].queryset = User.objects.filter(company=user.company).exclude(id=user.id)
        self.fields["receiver"].required = True

        self.fields["core_values"].queryset = CoreValue.objects.filter(company=user.company)
        self.fields["core_values"].required = True

        self.fields["message"].widget = forms.Textarea(
            attrs={"placeholder": "Write your message...", "required": "true"}
        )


class CreateUpdateCoreValueForm(forms.ModelForm):
    """
    Form to create or update a core value.
    """
    class Meta:
        model = CoreValue
        fields = ["name"]

    def __init__(self, *args, **kwargs):
        self.company = kwargs.pop("company", None)
        super().__init__(*args, **kwargs)
        self.fields["name"].widget.attrs.update({"placeholder": "Enter core value name"})

        # Trust instance.company if editing
        if self.instance and self.instance.pk:
            self.company = self.instance.company

    def clean_name(self):
        name = self.cleaned_data.get("name", "").strip().casefold()

        qs = CoreValue.objects.filter(company=self.company, name__iexact=name)
        if self.instance.pk:
            qs = qs.exclude(pk=self.instance.pk)

        if qs.exists():
            raise forms.ValidationError("A core value with this name already exists.")

        return name

    def save(self, commit=True):
        core_value = super().save(commit=False)

        # Only set company if this is a new object
        if not core_value.pk:
            core_value.company = self.company

        # Capitalize name properly
        core_value.name = self.cleaned_data["name"].title()

        if commit:
            core_value.save()
        return core_value
