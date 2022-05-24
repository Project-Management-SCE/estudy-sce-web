from django.shortcuts import redirect, render
from django.views import View
from category.models import HomeWork, YouTubeVideo
from category.form import CourseForm, HomeWorkForm, CreatCourseForm, CommentHomeWorkForm
from category.models import Course, CommentHomeWork
from accounts.models import Student, User

class CategoryView(View):
  def get(self,request,user_id):
    form = CourseForm()
    if request.user.is_student:
        user = User.objects.get(pk=user_id)
        student = Student.objects.get(user=user)
        form = CourseForm(instance=student)
    return render(request,"category.html",{'form':form})
  def post(self,request):
    pass
  
  
  
  
  
  class ForumFileView(View):
    """
    ForumFileView
    """

    def get(self, request, hw_id):
        hw = HomeWork.objects.get(pk=hw_id)
        comments = CommentHomeWork.objects.filter(hw=hw).iterator()
        comment = CommentHomeWorkForm()
        return render(
            request,
            "ForumFile.html",
            {"hw": hw, "comments": comments, "form_comment": comment},
        )
