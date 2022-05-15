from django.urls import path
from forum import views

app_name = "Forum"

urlpatterns = [
    path("", views.forumView.as_view(), name="forum-main"),
    path("<user_id>", views.forumView.as_view(), name="post-post"),
    path("<user_id>/<post_id>", views.PostComments, name="comment-post"),
]

