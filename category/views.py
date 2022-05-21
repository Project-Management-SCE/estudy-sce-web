from django.shortcuts import redirect, render
from django.views import View
from category.models import HomeWork
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

  def post(self,request,user_id):
    form = CourseForm(request.POST)
    if form.is_valid():
      depart = form.cleaned_data['department']
      year = form.cleaned_data['year']
      semester = form.cleaned_data['semester']
      kind_of = form.cleaned_data['kind_of']
      if Course.objects.filter(department=depart,year=year,semester=semester,kind_of=kind_of).exists():
        all_courses = Course.objects.filter(department=depart,year=year,semester=semester,kind_of=kind_of).values()
        return render(request,"category.html",{'form':form,'all_courses':all_courses})
      else:
        return render(request,"category.html",{"error":"No results have been found",'form':form})

    return render(request,"category.html",{'form':form})



class HomeWorksView(View):
    def get(self, request, course_id, user_id):
        if bool(request.GET):
            value = request.GET["selecting"]
            if value == "1":
                course = Course.objects.get(id=course_id)
                homeworks = (
                    HomeWork.objects.filter(course=course, ratings__isnull=False)
                ).order_by("-ratings__average")
                mylist = list(dict.fromkeys(homeworks))
                return render(
                    request, "HomeWorks.html", {"course": course, "homeworks": mylist}
                )
            elif value == "2":
                course = Course.objects.get(id=course_id)
                homeworks = (HomeWork.objects.filter(course=course)).order_by(
                    "-nameFile"
                )
                return render(
                    request,
                    "HomeWorks.html",
                    {"course": course, "homeworks": homeworks},
                )
            else:
                course = Course.objects.get(id=course_id)
                homeworks = HomeWork.objects.filter(course=course)
                return render(
                    request,
                    "HomeWorks.html",
                    {"course": course, "homeworks": homeworks},
                )
        else:
            course = Course.objects.get(id=course_id)
            homeworks = HomeWork.objects.filter(course=course)
        return render(
            request, "HomeWorks.html", {"course": course, "homeworks": homeworks}
        )


class UploadFileView(View):
    """
    UploadFileView
    """
    def get(self,request, course_id , user_id):
        form = HomeWorkForm(initial={'course': course_id})
        return render(request,"upload_file.html",{'form':form})
    
    def post(self,request ,course_id, user_id):
        form = HomeWorkForm(request.POST, request.FILES)
        if form.is_valid():
            user = User.objects.get(id=user_id)
            file = request.FILES.get('file')
            homework = HomeWork.objects.create(nameFile=form.cleaned_data['nameFile'], file=file, course=form.cleaned_data['course'],user=user)
            homework.save()
            return redirect('Category:homework',course_id ,user_id)
        return render(request,"upload_file.html",{'form':form})



      
      
def deleteCourse(request, course_id):
    course = Course.objects.get(pk=course_id)
    course.delete()
    return redirect("Category:cat", request.user.id)

   
      
def deleteFile(request,course_id,hw_id ):
  hw = HomeWork.objects.get(pk=hw_id)
  hw.delete()
  return redirect('Category:homework',course_id, request.user.id)




class CreateCourseView(View):
    def get(self, request):
        form = CourseForm()
        folder = CreatCourseForm()
        return render(request, "category.html", {"folder": folder, "form": form})

    def post(self, request):
        form = CreatCourseForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("Category:cat", request.user.id)
