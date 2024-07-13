from django.contrib import admin
from apps.users.models import Sponsor, Student


@admin.register(Sponsor)
class SponsorAdmin(admin.ModelAdmin):
    list_display = ['sponsor_type', 'full_name', 'phone_number', 'amount', 'company_name', 'payment_type', 'status',
                    'spand_amount', 'created_at', ]
    list_display_links = list_display


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'phone_number', 'place_of_study', 'level', 'contract', 'sponsored_amount',
                    'created_at', ]
    list_display_links = list_display
