from django.contrib import admin
from appointments.models import Appointment


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ("patient_name", "appointment_date", "doctor", "phone")
    search_fields = ("patient_name", "phone", "diagnosis")
    list_filter = ("appointment_date", "doctor")
    date_hierarchy = "appointment_date"
    autocomplete_fields = ("doctor",)
