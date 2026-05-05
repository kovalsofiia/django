from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView

from doctors.forms import DoctorForm
from doctors.models import Doctor


class DoctorListView(ListView):
    model = Doctor
    template_name = "doctors/doctor_list.html"
    context_object_name = "doctors"


class DoctorCreateView(LoginRequiredMixin, CreateView):
    model = Doctor
    form_class = DoctorForm
    template_name = "doctors/doctor_form.html"
    success_url = reverse_lazy("doctors:doctor_list")


class DoctorUpdateView(LoginRequiredMixin, UpdateView):
    model = Doctor
    form_class = DoctorForm
    template_name = "doctors/doctor_form.html"
    success_url = reverse_lazy("doctors:doctor_list")
