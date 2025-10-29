from django.urls import path
from . import views

app_name = "booking"  # ← CRITICAL!

urlpatterns = [
    path("", views.book_table, name="book_table"),
    path("my_bookings/", views.my_bookings, name="my_bookings"),
    path("edit/<int:pk>/", views.edit_booking, name="edit_booking"),
    path("delete/<int:pk>/", views.delete_booking, name="delete_booking"),
]
