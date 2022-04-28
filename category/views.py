from django.shortcuts import redirect, render
from django.views import View
from category.models import HomeWork, YouTubeVideo
from category.form import CourseForm, HomeWorkForm, CreatCourseForm
from category.models import Course 
from accounts.models import Student, User 
# Create your views here.



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