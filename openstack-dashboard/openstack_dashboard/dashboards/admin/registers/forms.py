import logging
import re

from django.forms import ValidationError
from django.utils.translation import force_unicode, ugettext_lazy as _
from django.views.decorators.debug import sensitive_variables

from horizon import exceptions
from horizon import forms
from horizon import messages
from horizon.utils import validators

LOG = logging.getLogger(__name__)


class RegistrationForm(forms.Form):
    username = forms.CharField(label=_("User Name"))
    realname = forms.CharField(label=_("Real Name"))
    department = forms.CharField(label=_("Department"))
    email = forms.EmailField(label=_("Email"))
    password = forms.RegexField(
            label=_("Password"),
            widget=forms.PasswordInput(render_value=False),
            regex=validators.password_validator(),
            error_messages={'invalid': validators.password_validator_msg()})
    confirm_password = forms.CharField(
            label=_("Confirm Password"),
            required=False,
            widget=forms.PasswordInput(render_value=False))

    def clean_username(self):
        username = self.cleaned_data['username']
	if not re.search(u'^([a-zA-Z0-9])+',username):
            raise forms.ValidationError("User Name is illegal.")
        return username
    
    def clean_email(self):
        email = self.cleaned_data['email']
        if not re.search(u'^[a-z]([a-z0-9]*[-_\.]?[a-z0-9]+)*@([a-z0-9]*[-_]?[a-z0-9]+)+[\.][a-z]{2,3}([\.][a-z]{2})?$',email):
	    raise forms.ValidationError("Email Format is incorrect.")
        return email

    def clean_confirm_password(self):
        if 'password' in self.cleaned_data:
            password = self.cleaned_data['password']
            confirm_password = self.cleaned_data['confirm_password']
            if password == confirm_password:
                return password
            raise ValidationError(_('Passwords do not match.'))

