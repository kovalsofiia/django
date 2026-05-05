from datetime import timedelta

from django import forms
from django.utils import timezone

from appointments.models import Appointment


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = [
            "patient_name",
            "birth_date",
            "phone",
            "complaints",
            "appointment_date",
            "doctor",
            "diagnosis",
            "treatment_description",
        ]
        widgets = {
            "appointment_date": forms.DateTimeInput(attrs={"type": "datetime-local"}),
            "birth_date": forms.DateInput(attrs={"type": "date"}),
        }

    def clean_patient_name(self):
        patient_name = self.cleaned_data["patient_name"].strip()
        if len(patient_name) < 5:
            raise forms.ValidationError("ПІБ пацієнта має містити щонайменше 5 символів.")
        return patient_name

    def clean_appointment_date(self):
        appointment_date = self.cleaned_data["appointment_date"]
        if appointment_date < timezone.now() - timedelta(days=3650):
            raise forms.ValidationError("Дата прийому виглядає некоректною.")
        return appointment_date

