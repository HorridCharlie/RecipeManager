from django.http import Http404
from django.shortcuts import redirect, render, HttpResponse, get_object_or_404
from ..models import Category


def category(request, pk):
    try:
        category = get_object_or_404(Category, pk=pk)
        return render(request, "recipes/category.html", {"category": category})
    except Http404:
        return render(request, "recipes/error.html", {"error_title": "page not found",
                                                      "error_text1": "Sorry, but the page you requested cannot be found.",
                                                      "error_text2": "Try checking the URL for errors, then hit the refresh button on your browser."})
