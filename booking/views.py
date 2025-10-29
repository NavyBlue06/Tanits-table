from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .forms import BookingForm
from .models import Booking

@login_required
def book_table(request):
    if request.method == "POST":
        form = BookingForm(request.POST, user=request.user)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()
            return redirect("booking:my_bookings")
    else:
        form = BookingForm(user=request.user)  # ← PASS USER!
    return render(request, "booking/book.html", {"form": form})


@login_required
def my_bookings(request):
    bookings = Booking.objects.filter(user=request.user).order_by("date", "time")
    return render(request, "booking/my_bookings.html", {"bookings": bookings})


@login_required
def edit_booking(request, pk):
    booking = get_object_or_404(Booking, pk=pk, user=request.user)
    if request.method == "POST":
        form = BookingForm(request.POST, instance=booking, user=request.user)
        if form.is_valid():
            form.save()
            return redirect("booking:my_bookings")
    else:
        form = BookingForm(instance=booking, user=request.user)
    return render(
        request, "booking/edit_booking.html", {"form": form, "booking": booking}
    )


@login_required
def delete_booking(request, pk):
    booking = get_object_or_404(Booking, pk=pk, user=request.user)
    if request.method == "POST":
        booking.delete()
        return redirect("booking:my_bookings")
    return render(request, "booking/delete_booking.html", {"booking": booking})
