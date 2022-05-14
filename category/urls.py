from django.urls import path
from category import views

app_name = "Category"

urlpatterns = [
    path('<user_id>', views.CategoryView.as_view(), name="cat"),
    path('course/<course_id>/<user_id>',views.HomeWorksView.as_view(), name="homework"),
    path('upload-file/<course_id>/<user_id>',views.UploadFileView.as_view(), name="u-f"),
    path("del/<course_id>", views.deleteCourse, name="delete-course"),
    path('delfile/<course_id>/<hw_id>',views.deleteFile ,name="delete-file"),
]
