from django.core.validators import MinValueValidator
from django.db import models


class Doctor(models.Model):
    full_name = models.CharField(max_length=255, verbose_name="ПІБ")
    specialization = models.CharField(max_length=150, verbose_name="Спеціалізація")
    experience_years = models.PositiveIntegerField(
        validators=[MinValueValidator(0)],
        verbose_name="Стаж (років)",
    )

    class Meta:
        verbose_name = "Лікар"
        verbose_name_plural = "Лікарі"
        ordering = ["-experience_years", "full_name"]

    def __str__(self):
        return f"{self.full_name} ({self.specialization})"
