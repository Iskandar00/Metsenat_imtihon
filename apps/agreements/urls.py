from django.urls import path

from apps.agreements.views import AgreementCreateView, AgreementUpdateView, AgreementDeleteView

urlpatterns = [
    path('agreements_create/', AgreementCreateView.as_view(), name='agreements_create'),
    path('agreements/<int:pk>/', AgreementUpdateView.as_view(), name='agreements_delete'),
    path('agreements/<int:pk>/', AgreementDeleteView.as_view(), name='agreements_update'),

]