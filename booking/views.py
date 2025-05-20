from django.shortcuts import render, redirect
from .forms import BookingForm

def book_table(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = BookingForm()
    return render(request, "booking/book.html", {"form": form})
