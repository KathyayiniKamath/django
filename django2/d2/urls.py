from django.urls import path
from . import views

urlpatterns = [
    path('d2/',views.d2, name="d2"),
]
