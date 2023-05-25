from django.contrib import admin
from django.urls import path
from recipe import views

# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]


app_name = 'recipe'

urlpatterns = [
    path('', views.main, name='main'),
    path('main/', views.main, name='main'),
    path('recipe_detail/<int:recipe_id>/', views.recipe_detail, name='recipe_detail'),
]