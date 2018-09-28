from core.models import Watches, NameBrand
import django_filters
from django import forms

class WatchesFilterTest(django_filters.FilterSet):
    price = django_filters.NumberFilter()
    price__gt = django_filters.NumberFilter(field_name='price', lookup_expr='gt')
    price__lt = django_filters.NumberFilter(field_name='price', lookup_expr='lt')
    brand = django_filters.ModelMultipleChoiceFilter(queryset=NameBrand.objects.all(),
        widget=forms.CheckboxSelectMultiple)
    
    class Meta:
        model = Watches
        fields = ['price', 'namebrand']

    