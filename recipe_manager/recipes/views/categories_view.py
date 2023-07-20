from django.http import Http404
from django.shortcuts import redirect, render, HttpResponse, get_object_or_404
from django.utils import timezone
from ..models import Category
from ..forms import CategoryForm


def categories_list(request):
    try:
        categories = Category.objects.all()
        return render(request, 'categories/categories_list.html', {'categories': categories})
    except Http404:
        return render(request, "categories/error.html", {"error_title": "page not found",
                                                         "error_text1": "Sorry, but the page you requested cannot be found.",
                                                         "error_text2": "Try checking the URL for errors, then hit the refresh button on your browser."})


def category_detail(request, pk):
    try:
        category = get_object_or_404(Category, pk=pk)
        return render(request, "categories/category_detail.html", {"category": category})
    except Http404:
        return render(request, "categories/error.html", {"error_title": "page not found",
                                                         "error_text1": "Sorry, but the page you requested cannot be found.",
                                                         "error_text2": "Try checking the URL for errors, then hit the refresh button on your browser."})


def category_new(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            try:
                category = form.save(commit=False)
                category.name = request.user
                category.save()
                return redirect('category_detail', pk=category.pk)
            except ValueError:
                return render(request, "categories/error.html", {"error_title": "wrong author",
                                                                 "error_text1": "Sorry, but the page you requested cannot be found.",
                                                                 "error_text2": "Try checking the URL for errors, then hit the refresh button on your browser."})
    else:
        form = CategoryForm()
    return render(request, 'categories/category_edit.html', {'form': form})


def category_edit(request, pk):
    try:
        category = get_object_or_404(Category, pk=pk)
        if request.method == "POST":
            form = CategoryForm(request.POST, instance=category)
            if form.is_valid():
                category = form.save(commit=False)
                category.name = request.user
                category.save()
                return redirect('category_detail', pk=category.pk)
        else:
            form = CategoryForm(instance=category)
            return render(request, 'categories/category_edit.html', {'form': form})
    except Http404:
        return render(request, "categories/error.html", {"error_title": "page not found",
                                                         "error_text1": "Sorry, but the page you requested cannot be found.",
                                                         "error_text2": "Try checking the URL for errors, then hit the refresh button on your browser."})
