from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, DetailView, ListView, UpdateView

from appointments.forms import AppointmentForm
from appointments.models import Appointment
from hospital_project.auth_utils import GroupRequiredMixin, is_doctor


class AppointmentListShortView(ListView):
    """
    Коротка версія: ПІБ пацієнта, дата прийому, лікар, діагноз.
    Опціонально підтримує фільтрацію за діагнозом через ?diagnosis=...
    """

    model = Appointment
    template_name = "appointments/appointment_list_short.html"
    context_object_name = "appointments"
    diagnosis_cookie_name = "appointment_diagnosis_filter"

    def get_queryset(self):
        queryset = super().get_queryset()
        diagnosis = self.request.GET.get("diagnosis")
        if diagnosis is None:
            diagnosis = self.request.COOKIES.get(self.diagnosis_cookie_name, "").strip()

        self.active_diagnosis_filter = diagnosis or ""
        if diagnosis:
            queryset = queryset.filter(diagnosis__icontains=diagnosis)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["active_diagnosis_filter"] = self.active_diagnosis_filter
        context["can_edit_appointments"] = is_doctor(self.request.user)
        return context

    def get(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()
        context = self.get_context_data()
        response = self.render_to_response(context)

        if "diagnosis" in request.GET:
            response.set_cookie(self.diagnosis_cookie_name, self.active_diagnosis_filter, max_age=60 * 60 * 24 * 30)
        elif "clear_filter" in request.GET:
            response.delete_cookie(self.diagnosis_cookie_name)

        return response


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

    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        request.session["last_viewed_appointment_id"] = self.object.pk
        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["can_edit_appointments"] = is_doctor(self.request.user)
        return context


class AppointmentCreateView(CreateView):
    model = Appointment
    form_class = AppointmentForm
    template_name = "appointments/appointment_form.html"
    success_url = reverse_lazy("appointments:appointment_list_short")


class AppointmentUpdateView(GroupRequiredMixin, UpdateView):
    group_name = "doctor"
    model = Appointment
    form_class = AppointmentForm
    template_name = "appointments/appointment_form.html"
    success_url = reverse_lazy("appointments:appointment_list_short")


class AppointmentLastViewedRedirectView(View):
    def get(self, request, *args, **kwargs):
        appointment_id = request.session.get("last_viewed_appointment_id")
        if appointment_id:
            return redirect("appointments:appointment_detail", pk=appointment_id)
        return HttpResponseRedirect(reverse_lazy("appointments:appointment_list_short"))

