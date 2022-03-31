from django.urls import path
from users_app import views

urlpatterns = [
    path('test/', views.index, name='index')
]
