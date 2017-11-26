from django.shortcuts import render

from ssmais.search.views import ProviderSearchAndList
from ssmais.search.forms import SearchForm


class ProviderSearchName(ProviderSearchAndList):
    template_name = 'list_provider.html'
    form_request = SearchForm
