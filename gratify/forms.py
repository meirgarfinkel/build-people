from django import forms
from django.contrib.auth import get_user_model
from gratify.models import Recognition

User = get_user_model()

class CreateRecognitionForm(forms.ModelForm):
    class Meta:
        model = Recognition
        fields = ["receiver", "message", "points"]
    
    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user", None)
        super().__init__(*args, **kwargs)
        # Limit receiver choices to users in the same company as the giver,
        # and exclude the current user
        self.fields["receiver"].queryset = User.objects.filter(company=user.company).exclude(id=user.id)
