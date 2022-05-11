from django.urls import path
from forum import views

app_name = "Forum"

urlpatterns = [
    path("", views.forumView.as_view(), name="forum-main"),
]
