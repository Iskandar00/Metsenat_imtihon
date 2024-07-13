from django import forms

from apps.users.models import Sponsor, Student


class SponsorForm(forms.ModelForm):
    class Meta:
        model = Sponsor
        fields = ['sponsor_type', 'full_name', 'phone_number', 'amount', 'company_name', 'payment_type', ]


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['full_name', 'phone_number', 'place_of_study', 'level', 'contract', ]
