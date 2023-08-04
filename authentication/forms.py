# authentication/forms.py

from django.contrib.auth.forms import UserCreationForm, PasswordResetForm

class CustomUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Remove the help text for all fields
        for field_name in self.fields:
            self.fields[field_name].help_text = None

class CustomPasswordResetForm(PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Remove the help text for all fields
        for field_name in self.fields:
            self.fields[field_name].help_text = None
