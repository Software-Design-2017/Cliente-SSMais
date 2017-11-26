from django.conf.urls import url
from .views import (
    ClientRegisterView,
    CountConfirmation,
)

urlpatterns = (
    url(r'^register_client/', ClientRegisterView.register_client,
        name='register_client_view'),
    url(r'^confirm/(?P<activation_key>\w+)/', CountConfirmation.register_confirm, name='confirm_account'),
)
