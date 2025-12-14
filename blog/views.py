from django.shortcuts import render
from django.http import HttpResponse


# VIEWS


def blog(request):
    return HttpResponse("Hello, blog!")

