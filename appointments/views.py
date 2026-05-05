from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, UpdateView

from appointments.forms import AppointmentForm
from appointments.models import Appointment


class AppointmentListShortView(ListView):
    """
    Коротка версія: ПІБ пацієнта, дата прийому, лікар, діагноз.
    Опціонально підтримує фільтрацію за діагнозом через ?diagnosis=...
    """

    model = Appointment
    template_name = "appointments/appointment_list_short.html"
    context_object_name = "appointments"

    def get_queryset(self):
        queryset = super().get_queryset()
        diagnosis = self.request.GET.get("diagnosis")
        if diagnosis:
            queryset = queryset.filter(diagnosis__icontains=diagnosis)
        return queryset


class AppointmentListFullView(ListView):
    """
    Повна версія: усі поля запису.
    """

    model = Appointment
    template_name = "appointments/appointment_list_full.html"
    context_object_name = "appointments"


class AppointmentDetailView(DetailView):
    """
    Детальна сторінка одного запису (можна використовувати як ще одну «повну» версію).
    """

    model = Appointment
    template_name = "appointments/appointment_detail.html"
    context_object_name = "appointment"


class AppointmentCreateView(LoginRequiredMixin, CreateView):
    model = Appointment
    form_class = AppointmentForm
    template_name = "appointments/appointment_form.html"
    success_url = reverse_lazy("appointments:appointment_list_short")


class AppointmentUpdateView(LoginRequiredMixin, UpdateView):
    model = Appointment
    form_class = AppointmentForm
    template_name = "appointments/appointment_form.html"
    success_url = reverse_lazy("appointments:appointment_list_short")

