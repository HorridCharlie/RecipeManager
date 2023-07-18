from django.contrib import admin
from .models import Category, Chef, Ingredient, Recipe

admin.site.register(Category)
admin.site.register(Chef)
admin.site.register(Ingredient)
admin.site.register(Recipe)
