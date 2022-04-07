from django.urls import path
from accounts import views


app_name = 'accounts'

urlpatterns = [
    path('SignUp/', views.signUp, name='signup'),
    path('LogIn/', views.log_in, name='logIn'),
]
