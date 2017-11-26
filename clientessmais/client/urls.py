from django.conf.urls import url


from client.views import (ProviderSearchName)


urlpatterns = [
         url(r'^$', ProviderSearchName.as_view(), name="search_provider"),
]
