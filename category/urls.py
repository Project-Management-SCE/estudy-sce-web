from django.urls import path
from category import views

app_name = "Category"

urlpatterns = [
    path('<user_id>', views.CategoryView.as_view(), name="cat"),
    path("forumFile/<hw_id>", views.ForumFileView.as_view(), name="forum-file"),
    
]
