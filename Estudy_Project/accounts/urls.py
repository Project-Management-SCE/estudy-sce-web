from django.urls import path
from django.views.generic import TemplateView

from . import views

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signUp, name='signup'),
    path('login/', views.log_in, name='logIn'),
    path('',TemplateView.as_view(template_name="accounts/thankYou.html"), name="thank-you"),
]
