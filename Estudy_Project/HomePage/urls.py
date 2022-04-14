
from django.urls import path, include
from . import views


app_name = "HomePage"

urlpatterns = [
    path('',views.indexView.as_view(), name="home"),
    path('about/',views.aboutView.as_view(),name="about"),
    path('Delete/<post_id>',views.deletePost,name='delete-post'),
    path('update/<post_id>',views.updatePost,name='update-post'),
]
