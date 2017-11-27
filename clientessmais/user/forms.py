import logging
# Django.
from django import forms
from django.utils.translation import ugettext_lazy as _

# Local Django.
from .models import Client
from . import constants

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('EmbelezaMais')


class ClientRegisterForm(forms.ModelForm):
    # Form Fields.
    name = forms.CharField(label='NAME',
                           max_length=60)

    email = forms.EmailField(label='EMAIL')

    password = forms.CharField(widget=forms.PasswordInput,
                               label='PASSWORD')

    password_confirmation = forms.CharField(widget=forms.PasswordInput,
                                            label='PASSWORD CONFIRMATION')

    phone_number = forms.CharField(label='PHONE',
                                   max_length=14)

    class Meta:
        model = Client
        fields = [
            'name',
            'email',
            'phone_number'
        ]

    # Front-end validation function for client register page.
    def clean(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        password_confirmation = self.cleaned_data.get('password_confirmation')
        phone_number = self.cleaned_data.get('phone_number')

        email_from_database = Client.objects.filter(email=email)

        if email_from_database.exists():
            raise forms.ValidationError(('Email already registered'))
        elif len(password) < 8:
            raise forms.ValidationError(
                ('Password must be between 8 and 12 characters'))
        elif len(password) > 12:
            raise forms.ValidationError(
                ('Password must be between 8 and 12 characters'))
        elif password != password_confirmation:
            raise forms.ValidationError(('Passwords do not match.'))
        elif len(phone_number) > 14:
            raise forms.ValidationError(('Invalid phone number.'))

        return super(ClientRegisterForm, self).clean(*args, **kwargs)


class ClientLoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(
        widget=forms.PasswordInput, label=_(constants.PASSWORD))

    def clean(self, *args, **kwargs):
        password = self.cleaned_data.get("password")

        if len(password) < constants.PASSWORD_MIN_LENGTH:
            raise forms.ValidationError(
                {'password': [_(constants.PASSWORD_SIZE)]})
        elif len(password) > constants.PASSWORD_MAX_LENGTH:
            raise forms.ValidationError(
                {'password': [_(constants.PASSWORD_SIZE)]})
        else:
            pass

        return super(ClientLoginForm, self).clean(*args, **kwargs)

    class Meta:
        model = Client
