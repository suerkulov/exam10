from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError


class MyUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = ("username", "password1", "password2", "email", "first_name", "last_name")

    def clean_email(self):
        if self.cleaned_data.get("email") == '':
            raise ValidationError("Введите свою почту")
        return self.cleaned_data.get("email")