from django.http import Http404
from django.shortcuts import redirect, render, HttpResponse, get_object_or_404
from django.utils import timezone
from ..models import Chef
from ..forms import ChefForm


def chefs_list(request):
    try:
        chefs = Chef.objects.all()
        return render(request, 'chefs/chefs_list.html', {'chefs': chefs})
    except Http404:
        return render(request, "chefs/error.html", {"error_title": "page not found",
                                                    "error_text1": "Sorry, but the page you requested cannot be found.",
                                                    "error_text2": "Try checking the URL for errors, then hit the refresh button on your browser."})


def chef_detail(request, pk):
    try:
        chef = get_object_or_404(Chef, pk=pk)
        return render(request, "chefs/chef_detail.html", {"chef": chef})
    except Http404:
        return render(request, "chefs/error.html", {"error_title": "page not found",
                                                    "error_text1": "Sorry, but the page you requested cannot be found.",
                                                    "error_text2": "Try checking the URL for errors, then hit the refresh button on your browser."})


def chef_new(request):
    if request.method == "POST":
        form = ChefForm(request.POST)
        if form.is_valid():
            try:
                chef = form.save(commit=False)
                chef.name = request.user
                chef.bio = request.user
                chef.save()
                return redirect('chef_detail', pk=chef.pk)
            except ValueError:
                return render(request, "chef/error.html", {"error_title": "wrong author",
                                                           "error_text1": "Sorry, but the page you requested cannot be found.",
                                                           "error_text2": "Try checking the URL for errors, then hit the refresh button on your browser."})
    else:
        form = ChefForm()
    return render(request, 'chefs/chef_edit.html', {'form': form})


def chef_edit(request, pk):
    try:
        chef = get_object_or_404(Chef, pk=pk)
        if request.method == "POST":
            form = ChefForm(request.POST, instance=chef)
            if form.is_valid():
                chef = form.save(commit=False)
                chef.name = request.user
                chef.bio = request.user
                chef.save()
                return redirect('chef_detail', pk=chef.pk)
        else:
            form = ChefForm(instance=chef)
            return render(request, 'chefs/chef_edit.html', {'form': form})
    except Http404:
        return render(request, "chefs/error.html", {"error_title": "page not found",
                                                    "error_text1": "Sorry, but the page you requested cannot be found.",
                                                    "error_text2": "Try checking the URL for errors, then hit the refresh button on your browser."})
