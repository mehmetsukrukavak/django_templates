from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse


def index(request):
    return render(request, "template_app/first.html")


def weather_view(request):
    weather_dict = {
        "istanbul": "30",
        "ankara": "26",
        "paris": [3, 15, 16, 5],
        "rome": {"morning": 10, "evening": 15},
        "user_premium": True,
        "test": "Test Test test tEst"
    }
    return render(request, "template_app/weather.html", context=weather_dict)


