
from ssmais.search_scheduling.views import (
    ProviderSearchAndList, SearchDecorator, SearchName
)

from ssmais.search_scheduling.forms import SearchForm


from .forms import SearchFormType

class ProviderSearchName(ProviderSearchAndList):
    template_name = 'list_provider.html'
    form_request = SearchForm


class SearchType(SearchDecorator):
    def __init__(self, search, type_item, **kwargs):
         self.search = search
         self.type_item = type_item

    def refine_search(self):
        if self.type_item:
            list_itens = filter(self.verify_attr, self.get_list_itens())
            self.set_list_itens(list_itens)

    def verify_attr(self, provider):
        if(hasattr(provider,self.type_item)):
            return True
        else:
            return False

class ServiceSearchNameType(ProviderSearchAndList):
    template_name = 'list_service.html'
    form_request = SearchFormType
    type_item = None
    type_search = 'service'

    def get_fields(self, form):
        self.name = form.cleaned_data.get('name')
        self.type_item = form.cleaned_data.get('type_item')

    def define_researches(self):
        search = SearchName(name=self.name, type_search=self.type_search)
        search_refine = SearchType(search=search, type_item=self.type_item)
        print(self.type_item)
        return search_refine
