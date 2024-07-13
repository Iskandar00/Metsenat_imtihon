from django.urls import path

from apps.general.views import HomePage

urlpatterns = [
    path('', HomePage.as_view(), name='home_page')
]