from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse


def index(request):
    return render(request, "template_app/first.html")


def weather_view(request):
    weather_dict = {
        "istanbul": "30",
        "ankara": "26",
        "paris": [10, 15, 20, 21],
        "rome": {"morning": 10, "evening": 15},
    }
    return render(request, "template_app/weather.html", context=weather_dict)


