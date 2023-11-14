from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse


def index(request):
    return render(request, "template_app/first.html")
    #return HttpResponse("Main Page")

