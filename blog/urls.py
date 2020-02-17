from django.urls import path
from . import views

# The view that handles the logic at the specific route ''
urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
]
