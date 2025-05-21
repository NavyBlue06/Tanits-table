from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Booking
from .forms import BookingForm


@login_required
def book_table(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()
            messages.success(request, "Booking created successfully.")
            return redirect("my_bookings")
    else:
        form = BookingForm()
    return render(request, "booking/book.html", {"form": form})


@login_required
def my_bookings(request):
    bookings = Booking.objects.filter(user=request.user).order_by("date")
    return render(request, "booking/my_bookings.html", {"bookings": bookings})


@login_required
def edit_booking(request, booking_id):
    booking = get_object_or_404(Booking, pk=booking_id, user=request.user)

    if request.method == "POST":
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            messages.success(request, "Your booking was updated successfully.")
            return redirect("my_bookings")
    else:
        form = BookingForm(instance=booking)

    return render(request, "booking/edit_booking.html", {"form": form})


@login_required
def delete_booking(request, booking_id):
    booking = get_object_or_404(Booking, pk=booking_id, user=request.user)
    if request.method == "POST":
        booking.delete()
        messages.success(request, "Your booking was deleted successfully.")
        return redirect("my_bookings")
    return render(request, "booking/delete_booking.html", {"booking": booking})
