from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView

from apps.agreements.models import Agreement
from apps.agreements.forms import AgreementForm


class AgreementCreateView(CreateView):
    model = Agreement
    form_class = AgreementForm
    template_name = 'agreements.html'
    success_url = reverse_lazy('home_page')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_id = self.request.GET.get('user_id')
        context['users'] = Agreement.objects.all()
        context['user_detail'] = Agreement.objects.filter(id=user_id).first()
        context['student_or_sponsor_create'] = 'By sponsors giving money to students'
        return context


class AgreementUpdateView(UpdateView):
    model = Agreement
    form_class = AgreementForm
    template_name = 'users_update.html'
    success_url = reverse_lazy('agreements_create')


class AgreementDeleteView(DeleteView):
    template_name = 'delete.html'
    model = Agreement
    success_url = reverse_lazy('agreements_create')
