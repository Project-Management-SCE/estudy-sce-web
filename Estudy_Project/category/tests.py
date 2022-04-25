from django.test import TestCase
from category.models import Course, HomeWork, YouTubeVideo
from category.models import User
# Create your tests here.

class CourseTest(TestCase):

  def test_default_assigment(self):
    course = Course.objects.create()
    self.assertEqual(course.department,"1")
    self.assertEqual(course.year,"1")
    self.assertEqual(course.semester,"1")
    self.assertEqual(course.kind_of,"1")
 
class HomeWorkTest(TestCase):
   def test_homework(self):
    user = User.objects.create(username="Dani")
    course = Course.objects.create()
    homework = HomeWork.objects.create(course=course,user=user, nameFile="חדוא")

    self.assertEqual(homework.user,user)
    self.assertEqual(homework.course,course)
    self.assertEqual(homework.nameFile,"חדוא")


#  user = models.ForeignKey(User,on_delete=models.CASCADE, null=True)
#   course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True)
#   nameFile = models.CharField('Name File',max_length=30)
#   file = models.FileField('File',upload_to="files",null=True)


# class Course(models.Model):
#   name_course = models.CharField(max_length=30,)
#   department = models.CharField(max_length=30, choices=DEPARTMENT_CHOICES,default="1",)
#   year = models.CharField(max_length=30, choices=YEAR_CHOICES,default="1")
#   semester = models.CharField(max_length=30,choices=SEMESTER_CHOICES,default="1")
#   kind_of = models.CharField(max_length=30,choices=KIND_CHOICES,default="1")
