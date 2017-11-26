from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy

# Create your views here.
from ssmais.service.views import ServiceComboCreate
from ssmais.provider.models import Provider



class CreateCombo(ServiceComboCreate):
    template_name = 'combo_service_form.html'
    success_url = reverse_lazy('search_provider')


    def set_provider(self):
        # TODO USER
        providers = Provider.objects.all()
        self.provider = providers[0]
