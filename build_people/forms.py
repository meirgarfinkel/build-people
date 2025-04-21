from django import forms
from django.contrib.auth import get_user_model
from build_people.models import Recognition
from users.enums import RecognitionPoints

User = get_user_model()

class CreateRecognitionForm(forms.ModelForm):
    points = forms.ChoiceField(choices=RecognitionPoints, required=True, initial=RecognitionPoints.TEN)

    class Meta:
        model = Recognition
        fields = ["receiver", "message", "points"]

    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user", None)
        super().__init__(*args, **kwargs)

        # Limit receiver choices to users in the same company as the giver,
        # and exclude the current user
        self.fields["receiver"].queryset = User.objects.filter(company=user.company).exclude(id=user.id)
        self.fields["receiver"].required = True

        self.fields["message"].widget = forms.Textarea(
            attrs={"placeholder": "Write your message...", "required": "true"}
        )
