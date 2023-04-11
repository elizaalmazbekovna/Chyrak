from django.urls import path
from . import views

urlpatterns = [
    path('', views.add_person, name='create_person')
]