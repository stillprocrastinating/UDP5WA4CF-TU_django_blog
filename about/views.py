from django.shortcuts import render
from .models import About


def about_me(request):
    """
    Renders the About page
    """

    about = About.objects.all().order_by('-updated_on').first()

    context = {
        "about": about
    }

    return render(
        request,
        "about/about.html",
        context,
    )
