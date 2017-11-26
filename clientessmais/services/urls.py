from django.conf.urls import url


from services.views import (CreateCombo)


urlpatterns = [
         url(r'^$', CreateCombo.as_view(), name="create_combo"),
]
