from django.urls import path
from . import views

urlpatterns = [
    path('', views.recipes_list, name='recipes_list'),
    path('recipe/<int:pk>/', views.recipe_detail, name='recipe_detail'),
    path('recipe/<int:pk>/edit/', views.recipe_edit, name='recipe_edit'),
    path('recipe/new', views.recipe_new, name='recipe_new'),
    path('category/', views.category, name='category'),
    path('chef/', views.chef, name='chef'),
]
