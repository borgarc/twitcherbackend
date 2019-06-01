from django_filters.rest_framework import FilterSet, Filter
from people.models import Person

class PersonFilter(FilterSet):
    followed_by = Filter(field_name='followers', lookup_expr='in')

    class Meta:
        model = Person
        fields = ['followed_by']