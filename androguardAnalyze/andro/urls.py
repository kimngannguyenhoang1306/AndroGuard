from django.urls import path
from . import views

urlpatterns = [
    path("",  views.Analyze.as_view(), name="MainPage"),
]