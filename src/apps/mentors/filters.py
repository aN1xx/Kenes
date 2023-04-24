from django_filters import rest_framework as filters

from .models import Mentor


class MentorFilter(filters.FilterSet):
    first_name = filters.CharFilter(field_name='first_name', lookup_expr='icontains')
    last_name = filters.CharFilter(field_name='last_name', lookup_expr='icontains')
    middle_name = filters.CharFilter(field_name='middle_name', lookup_expr='icontains')
    about = filters.CharFilter(field_name='about', lookup_expr='icontains')
    occupation = filters.CharFilter(field_name='occupation', lookup_expr='icontains')
    grade = filters.CharFilter(field_name='grade', lookup_expr='icontains')

    class Meta:
        model = Mentor
        fields = ['first_name', 'last_name', 'middle_name', 'about', 'occupation', 'grade']
