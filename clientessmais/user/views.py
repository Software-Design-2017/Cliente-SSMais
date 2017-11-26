# standard library
import logging
import hashlib
import datetime
import random

# Django

from django.shortcuts import (
    render, redirect, get_object_or_404
)
from django.core.mail import send_mail
from django.utils import timezone
from django.http import HttpResponse
from django.views.generic import (
    View
)

# local Django
from .forms import (
    ClientRegisterForm,
)
from .models import (
    Client, UserProfile
)

from . import constants

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('EmbelezaMais')


class ClientRegisterView(View):
    def register_client(request):
        form = ClientRegisterForm(request.POST or None)
        if form.is_valid():
            logger.debug("Register form was valid.")
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            name = form.cleaned_data.get('name')
            phone_number = form.cleaned_data.get('phone_number')
            Client.objects.create_user(email=email, password=password,
                                       name=name, phone_number=phone_number)

            user = Client.objects.get(email=email)
            return CountConfirmation.send_email_confirmation(user)
        else:
            logger.debug("Register form was invalid.")

        return render(request, "client_register_form.html", {"form": form})


class CountConfirmation(View):
    def send_email_confirmation(user):
        # Prepare the information needed to send the account verification
        # email.
        salt = hashlib.sha1(str(random.random()).
                            encode('utf-8')).hexdigest()[:5]
        email = user.email

        activation_key = hashlib.sha1(str(salt+email).
                                      encode('utf‌​-8')).hexdigest()
        key_expires = datetime.datetime.today() + datetime.timedelta(2)

        new_profile = UserProfile(user=user, activation_key=activation_key,
                                  key_expires=key_expires)
        new_profile.save()

        # Send account confirmation email.
        email_subject = (constants.EMAIL_CONFIRMATION_SUBJECT)
        email_body = constants.EMAIL_CONFIRMATION_BODY % (activation_key)

        send_mail(email_subject, email_body, constants.EMBELEZAMAIS_EMAIL, [email],
                  fail_silently=False)

        logger.info("Email sended to user.")
        return redirect('/')

    def register_confirm(request, activation_key):
        # Check if activation token is valid, if not valid return an 404 error.
        # Verify if user is already confirmed.
        if request.user.id is not None:

            logger.info("Logged user: " + request.user.name)

            HttpResponse('Conta ja confirmada')
        else:
            # Nothing to do
            pass

        user_profile = get_object_or_404(UserProfile,
                                         activation_key=activation_key)

        # Verifies if the activation token has expired and if so renders the html
        # of expired registration.
        if user_profile.key_expires < timezone.now():
            user_profile.delete()

            return HttpResponse("Tempo para confirmar conta expirou." +
                                "Crie sua conta novamente")
        else:
            # Nothing to do.
            pass

        # If the token has not expired, the user is activated and the
        # confirmation html is displayed.
        user = user_profile.user
        user.is_active = True
        user.save()

        return redirect('/')
