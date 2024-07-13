from django import forms

from apps.agreements.models import Agreement


class AgreementForm(forms.ModelForm):
    class Meta:
        model = Agreement
        fields = ['sponsor', 'student', 'amount', ]

