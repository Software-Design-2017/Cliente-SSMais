
from ssmais.search_scheduling.views import ProviderSearchAndList
from ssmais.search_scheduling.forms import SearchForm


class ProviderSearchName(ProviderSearchAndList):
    template_name = 'list_provider.html'
    form_request = SearchForm
