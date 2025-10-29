from django.shortcuts import render


def index(request):
    return render(request, "home/index.html")


def menu(request):
    return render(request, "home/menu.html")

# CUSTOM ERROR HANDLERS


def custom_404(request, exception):
    return render(request, "404.html", status=404)


def custom_500(request):
    return render(request, "500.html", status=500)


def custom_403(request, exception):
    return render(request, "403.html", status=403)
