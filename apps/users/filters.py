import django_filters
from .models import Student, Sponsor


class StudentFilter(django_filters.FilterSet):
    class Meta:
        model = Student
        fields = ['place_of_study', 'level']


class SponsorFilter(django_filters.FilterSet):
    class Meta:
        model = Sponsor
        fields = ['sponsor_type', 'payment_type', 'status']
