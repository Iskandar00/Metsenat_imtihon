from django.contrib import admin
from apps.agreements.models import PlaceOfStudy, Agreement


@admin.register(PlaceOfStudy)
class PlaceOfStudyAdmin(admin.ModelAdmin):
    list_display = ['name', ]
    list_display_links = list_display


@admin.register(Agreement)
class AgreementAdmin(admin.ModelAdmin):
    list_display = ['sponsor', 'student', 'amount', ]
    list_display_links = list_display
