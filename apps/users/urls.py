from django.urls import path

from apps.users import views
urlpatterns = [
    path('sponsor_create/', views.SponsorCreateView.as_view(), name='sponsor_create'),
    path('student_create/', views.StudentCreateView.as_view(), name='student_create'),
    path('sponsor_delete/<int:pk>/', views.SponsorDeleteView.as_view(), name='sponsor_delete'),
    path('sponsor_update/<int:pk>/', views.SponsorUpdateView.as_view(), name='sponsor_update'),
    path('student_delete/<int:pk>/', views.StudentDeleteView.as_view(), name='student_delete'),
    path('student_update/<int:pk>/', views.StudentUpdateView.as_view(), name='student_update'),
]