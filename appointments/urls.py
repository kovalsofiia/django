from django.urls import path

from appointments.views import (
    AppointmentCreateView,
    AppointmentDetailView,
    AppointmentLastViewedRedirectView,
    AppointmentListFullView,
    AppointmentListShortView,
    AppointmentUpdateView,
)

app_name = "appointments"

urlpatterns = [
    path("", AppointmentListShortView.as_view(), name="appointment_list_short"),
    path("last/", AppointmentLastViewedRedirectView.as_view(), name="appointment_last_viewed"),
    path("add/", AppointmentCreateView.as_view(), name="appointment_add"),
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
    path("<int:pk>/edit/", AppointmentUpdateView.as_view(), name="appointment_edit"),
]

