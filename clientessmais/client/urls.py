from django.conf.urls import url


from client.views import (ServiceSearchNameType)
from client.views import (ProviderSearchName)


urlpatterns = [
         url(r'^service/$', ServiceSearchNameType.as_view(), name="search_service"),
         url(r'^provider/$', ProviderSearchName.as_view(), name="search_provider"),
]
