from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView

from apps.users.filters import StudentFilter, SponsorFilter
from apps.users.forms import SponsorForm, StudentForm
from apps.users.models import Sponsor, Student


class SponsorCreateView(CreateView):
    model = Sponsor
    form_class = SponsorForm
    template_name = 'sponsor_create.html'

    def get_success_url(self):
        referer_url = self.request.META.get('HTTP_REFERER')
        if referer_url:
            return referer_url
        else:
            return reverse_lazy('default_success_url')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_id = self.request.GET.get('user_id')
        context['user_detail'] = Sponsor.objects.filter(id=user_id).first()
        context['student_or_sponsor_create'] = 'Apply for sponsorship'

        context['users'] = Sponsor.objects.all()
        self.filterset = SponsorFilter(self.request.GET, queryset=context['users'])
        context['users'] = self.filterset.qs
        context['filter'] = self.filterset

        return context


class SponsorUpdateView(UpdateView):
    model = Sponsor
    form_class = SponsorForm
    template_name = 'users_update.html'
    success_url = reverse_lazy('sponsor_create')


class SponsorDeleteView(DeleteView):
    template_name = 'delete.html'
    model = Sponsor
    success_url = reverse_lazy('sponsor_create')


class StudentCreateView(CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'student_create.html'

    def get_success_url(self):
        referer_url = self.request.META.get('HTTP_REFERER')
        if referer_url:
            return referer_url
        else:
            return reverse_lazy('default_success_url')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_id = self.request.GET.get('user_id')
        context['user_detail'] = Student.objects.filter(id=user_id).first()
        context['student_or_sponsor_create'] = 'Student create'

        context['users'] = Student.objects.all()
        self.filterset = StudentFilter(self.request.GET, queryset=context['users'])
        context['users'] = self.filterset.qs
        context['filter'] = self.filterset

        return context


class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'users_update.html'
    success_url = reverse_lazy('student_create')


class StudentDeleteView(DeleteView):
    template_name = 'delete.html'
    model = Student
    success_url = reverse_lazy('student_create')
