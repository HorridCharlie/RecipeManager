from django.urls import path
from . import views

urlpatterns = [
    path('', views.recipes_list, name='recipes_list'),
    path('recipe/<int:pk>/', views.recipe_detail, name='recipe_detail'),
    path('recipe/<int:pk>/edit/', views.recipe_edit, name='recipe_edit'),
    path('recipe/new/', views.recipe_new, name='recipe_new'),
    path('categories', views.categories_list, name='categories_list'),
    path('category/<int:pk>/', views.category_detail, name='category_detail'),
    path('category/<int:pk>/edit/', views.category_edit, name='category_edit'),
    path('category/new/', views.category_new, name='category_new'),
    path('chefs', views.chefs_list, name='chefs_list'),
    path('chef/<int:pk>/', views.chef_detail, name='chef_detail'),
    path('chef/<int:pk>/edit/', views.chef_edit, name='chef_edit'),
    path('chef/new/', views.chef_new, name='chef_new'),
]
