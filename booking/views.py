# bookings/views.py
from datetime import date
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.db import IntegrityError
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from .forms import BookingForm
from .models import Booking


def home(request):
    """Render the public landing page."""
    return render(request, "home.html")


@login_required
def book_table(request):
    """Create a new booking."""
    if request.method == "POST":
        form = BookingForm(request.POST, user=request.user)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            try:
                booking.save()
            except IntegrityError:
                form.add_error(None, "A booking already exists for this date and time.")
            else:
                messages.success(request, "Table booking created successfully.")
                return redirect("my_bookings")
    else:
        initial = {
            "name": (
                f"{request.user.first_name} {request.user.last_name}".strip()
                or request.user.username
            ),
            "email": request.user.email,
        }
        form = BookingForm(initial=initial, user=request.user)

    return render(request, "bookings/book_table.html", {"form": form})


@login_required
def my_bookings(request):
    """List bookings belonging to the authenticated user."""
    bookings = Booking.objects.filter(user=request.user).order_by(
        "-date", "-time", "-id"
    )
    return render(request, "bookings/my_bookings.html", {"bookings": bookings})


@login_required
def edit_booking(request, pk):
    """Edit an existing booking belonging to the authenticated user."""
    booking = get_object_or_404(Booking, pk=pk)
    if booking.user_id != request.user.id:
        raise PermissionDenied("Access denied.")

    if request.method == "POST":
        form = BookingForm(request.POST, instance=booking, user=request.user)
        if form.is_valid():
            try:
                form.save()
            except IntegrityError:
                form.add_error(None, "A booking already exists for this date and time.")
            else:
                messages.success(request, "Booking updated successfully.")
                return redirect("my_bookings")
    else:
        form = BookingForm(instance=booking, user=request.user)

    return render(
        request, "bookings/edit_booking.html", {"form": form, "booking": booking}
    )


@login_required
def delete_booking(request, pk):
    """Delete a booking belonging to the authenticated user."""
    booking = get_object_or_404(Booking, pk=pk)
    if booking.user_id != request.user.id:
        raise PermissionDenied("Access denied.")

    if request.method == "POST":
        booking.delete()
        messages.success(request, "Booking deleted successfully.")
        return redirect("my_bookings")

    return render(request, "bookings/confirm_delete.html", {"booking": booking})
