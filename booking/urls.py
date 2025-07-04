from django.urls import path
from . import views

urlpatterns = [
    path("", views.book_table, name="booking"),
    path("my_bookings/", views.my_bookings, name="my_bookings"),
    path("edit/<int:booking_id>/", views.edit_booking, name="edit_booking"),
    path("delete/<int:booking_id>/", views.delete_booking, name="delete_booking"),
]
