from django.shortcuts import render, redirect
from django.contrib import messages
from .models import ContactMessage, CareerApplication


def home_view(request):
    return render(request, "index.html")


def about_view(request):
    return render(request, "about.html")


def products_view(request):
    return render(request, "products.html")


def networking_view(request):
    return render(request, "products/networking.html")


def security_view(request):
    return render(request, "products/security.html")


def wireless_view(request):
    return render(request, "products/wireless.html")


def software_view(request):
    return render(request, "products/software.html")


def solutions_view(request):
    return render(request, "solutions.html")


def contact_view(request):
    if request.method == "POST":
        ContactMessage.objects.create(
            name=request.POST.get("name"),
            email=request.POST.get("email"),
            phone=request.POST.get("phone"),
            subject=request.POST.get("subject"),
            message=request.POST.get("message"),
        )
        messages.success(request, "Your message has been sent successfully!")
        return redirect("contact")

    return render(request, "contact.html")


def careers_view(request):
    if request.method == "POST":
        CareerApplication.objects.create(
            full_name=request.POST.get("full_name"),
            email=request.POST.get("email"),
            phone=request.POST.get("phone"),
            position=request.POST.get("position"),
            resume=request.FILES.get("resume"),
        )
        messages.success(request, "Application submitted successfully!")
        return redirect("careers")

    return render(request, "careers.html")