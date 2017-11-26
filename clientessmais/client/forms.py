from ssmais.search_scheduling.forms import SearchForm
from django import forms

from . import constants


class SearchFormType(SearchForm):
    # Form Fields.
    type_item = forms.TypedChoiceField(choices=constants.TYPES_CHOICES,
                                       widget=forms.RadioSelect(attrs={'display': 'inline-block'}),
                                       label='Nome', required=False)
