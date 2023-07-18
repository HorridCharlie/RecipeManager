from django.http import Http404
from django.shortcuts import redirect, render, HttpResponse, get_object_or_404
from django.utils import timezone
from ..models import Recipe
from ..forms import RecipeForm


def recipes_list(request):
    try:
        recipes = Recipe.objects.filter(created_at__lte=timezone.now()).order_by('created_at')
        return render(request, 'recipes/recipes_list.html', {'recipes': recipes})
    except Http404:
        return render(request, "recipes/error.html", {"error_title": "page not found",
                                                      "error_text1": "Sorry, but the page you requested cannot be found.",
                                                      "error_text2": "Try checking the URL for errors, then hit the refresh button on your browser."})


def recipe_detail(request, pk):
    try:
        recipe = get_object_or_404(Recipe, pk=pk)
        return render(request, "recipes/recipe_detail.html", {"recipe": recipe})
    except Http404:
        return render(request, "recipes/error.html", {"error_title": "page not found",
                                                      "error_text1": "Sorry, but the page you requested cannot be found.",
                                                      "error_text2": "Try checking the URL for errors, then hit the refresh button on your browser."})


def recipe_new(request):
    if request.method == "POST":
        form = RecipeForm(request.POST)
        if form.is_valid():
            try:
                recipe = form.save(commit=False)
                recipe.chef = request.user
                recipe.created_at = timezone.now()
                recipe.save()
                return redirect('recipe_detail', pk=recipe.pk)
            except ValueError:
                return render(request, "recipes/error.html", {"error_title": "wrong author",
                                                              "error_text1": "Sorry, but the page you requested cannot be found.",
                                                              "error_text2": "Try checking the URL for errors, then hit the refresh button on your browser."})
    else:
        form = RecipeForm()
    return render(request, 'recipes/recipe_edit.html', {'form': form})


def recipe_edit(request, pk):
    try:
        recipe = get_object_or_404(Recipe, pk=pk)
        if request.method == "POST":
            form = RecipeForm(request.POST, instance=recipe)
            if form.is_valid():
                recipe = form.save(commit=False)
                recipe.chef = request.user
                recipe.created_at = timezone.now()
                recipe.save()
                return redirect('recipe_detail', pk=recipe.pk)
        else:
            form = RecipeForm(instance=recipe)
            return render(request, 'recipes/recipe_edit.html', {'form': form})
    except Http404:
        return render(request, "recipes/error.html", {"error_title": "page not found",
                                                      "error_text1": "Sorry, but the page you requested cannot be found.",
                                                      "error_text2": "Try checking the URL for errors, then hit the refresh button on your browser."})
