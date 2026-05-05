from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView

from doctors.forms import DoctorForm
from doctors.models import Doctor
from hospital_project.auth_utils import GroupRequiredMixin, is_administrator


class DoctorListView(ListView):
    model = Doctor
    template_name = "doctors/doctor_list.html"
    context_object_name = "doctors"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["can_manage_doctors"] = is_administrator(self.request.user)
        return context


class DoctorCreateView(GroupRequiredMixin, CreateView):
    group_name = "administrator"
    model = Doctor
    form_class = DoctorForm
    template_name = "doctors/doctor_form.html"
    success_url = reverse_lazy("doctors:doctor_list")


class DoctorUpdateView(GroupRequiredMixin, UpdateView):
    group_name = "administrator"
    model = Doctor
    form_class = DoctorForm
    template_name = "doctors/doctor_form.html"
    success_url = reverse_lazy("doctors:doctor_list")
