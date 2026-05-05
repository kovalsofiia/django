from django.contrib import admin
from doctors.models import Doctor


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ("full_name", "specialization", "experience_years")
    search_fields = ("full_name", "specialization")
    list_filter = ("specialization",)
