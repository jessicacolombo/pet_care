# app/urls.py
from django.urls import path
from .views import PetsViews, PetsComposedViews

urlpatterns = [
    path("pets/", PetsViews.as_view()),
    path("pets/<int:pet_id>/", PetsComposedViews.as_view()),
]
