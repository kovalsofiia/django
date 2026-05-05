from django.db import models
from doctors.models import Doctor


class Appointment(models.Model):
    patient_name = models.CharField(max_length=255, verbose_name="ПІБ пацієнта")
    birth_date = models.DateField(verbose_name="Дата народження")
    phone = models.CharField(max_length=20, verbose_name="Телефон")
    complaints = models.TextField(verbose_name="Скарги")
    appointment_date = models.DateTimeField(verbose_name="Дата та час прийому")
    doctor = models.ForeignKey(
        Doctor,
        on_delete=models.CASCADE,
        related_name="appointments",
        verbose_name="Лікар",
    )
    diagnosis = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name="Діагноз",
    )
    treatment_description = models.TextField(
        blank=True,
        null=True,
        verbose_name="Опис лікування",
    )

    class Meta:
        verbose_name = "Запис до лікаря"
        verbose_name_plural = "Записи до лікарів"
        ordering = ["appointment_date"]

    def __str__(self):
        formatted_date = self.appointment_date.strftime("%d.%m.%Y %H:%M")
        return f"{self.patient_name} -> {self.doctor.full_name} ({formatted_date})"
