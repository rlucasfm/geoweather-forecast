from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:cidade>/<str:pais>', views.getcidade, name="getcidade"),
]