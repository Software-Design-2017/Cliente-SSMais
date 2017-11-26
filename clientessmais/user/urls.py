from django.conf.urls import url
from .views import (
    ClientRegisterView,
    CountConfirmation,
    LoginClientView,
    LogoutView,
)

urlpatterns = (
    url(r'^register_client/', ClientRegisterView.register_client,
        name='register_client_view'),
    url(r'^confirm/(?P<activation_key>\w+)/', CountConfirmation.register_confirm, name='confirm_account'),
    url(r'^login_client/', LoginClientView.as_view(), name='login_client'),
    url(r'^logout/', LogoutView.as_view(), name='logout_view'),
)
