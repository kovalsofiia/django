from django.urls import path

from doctors.views import DoctorCreateView, DoctorListView, DoctorUpdateView

app_name = "doctors"

urlpatterns = [
    path("", DoctorListView.as_view(), name="doctor_list"),
    path("add/", DoctorCreateView.as_view(), name="doctor_add"),
    path("<int:pk>/edit/", DoctorUpdateView.as_view(), name="doctor_edit"),
]

