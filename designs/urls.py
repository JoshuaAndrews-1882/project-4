from django.urls import path
from . import views

urlpatterns = [
    path('', views.designs, name="designs"),
    path('design/<slug:pk>/', views.design, name="design"),
]