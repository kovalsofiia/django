from django.urls import path

from appointments.views import (
    AppointmentDetailView,
    AppointmentListFullView,
    AppointmentListShortView,
)

app_name = "appointments"

urlpatterns = [
    path("", AppointmentListShortView.as_view(), name="appointment_list_short"),
    path(
        "full/",
        AppointmentListFullView.as_view(),
        name="appointment_list_full",
    ),
    path(
        "<int:pk>/",
        AppointmentDetailView.as_view(),
        name="appointment_detail",
    ),
]

