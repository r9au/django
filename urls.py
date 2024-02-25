from django.contrib import admin
from django.urls import path,include
from cyber import views

urlpatterns = [
    path('sec/', views.cyber, name='cyber')
]
