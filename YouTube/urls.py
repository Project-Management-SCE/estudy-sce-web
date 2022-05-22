from django.urls import path
from YouTube import views

app_name = "YouTube"

urlpatterns = [
    path("", views.SearchVideoView.as_view(), name="youtube"),
]
