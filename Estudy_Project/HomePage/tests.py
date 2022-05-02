from datetime import datetime
from django.test import TestCase, tag
from django.urls import resolve, reverse
from accounts.models import User
from HomePage.models import Post
from HomePage.views import indexView , aboutView, searchView, updatePost ,DownPermissions, UpPermissions,deletePost,updatePost
# Create your tests here.



@tag('unit-test')
class HomePageUrlsTest(TestCase):
    def setUp(self):
      self.user2 = User.objects.create(username="nameTest")
      self.user = User.objects.create_superuser(email='test@test.com', username='test_create_super_user',
                                                  first_name='first name', last_name='last name', password="user password")
      self.post = Post.objects.create(title="testTitle", date=datetime.today(), description="TestTest")

    @tag('unit-test')
    def test_showHome(self):
        #Act
        url = reverse('HomePage:home')
        #Assert
        self.assertEqual(resolve(url).func.view_class, indexView)
   
    @tag('unit-test')
    def test_showAbout(self):
        #Act
        url = reverse('HomePage:about')
        #Assert
        self.assertEqual(resolve(url).func.view_class, aboutView)
    
    @tag('unit-test')
    def test_showDeletePost(self):
        #Act
        url = reverse('HomePage:delete-post', kwargs={'post_id':self.post.id})
        #Assert
        self.assertEqual(resolve(url).func, deletePost)
   
    @tag('unit-test')
    def test_showUpdate(self):
        #Act
        url = reverse('HomePage:update-post',kwargs={'post_id':self.post.id})
        #Assert
        self.assertEqual(resolve(url).func, updatePost)
    
    
    @tag('unit-test')
    def test_showSearchUser(self):
        #Act
        url = reverse('HomePage:search-user')
        #Assert
        self.assertEqual(resolve(url).func.view_class, searchView)

    @tag('unit-test')
    def test_showDownPermissions(self):
        #Act
        url = reverse('HomePage:down-per',kwargs={'user_id':self.user2.id})
        #Assert
        self.assertEqual(resolve(url).func.view_class, DownPermissions)
   
    @tag('unit-test')
    def test_showUpPermissions(self):
        #Act
        url = reverse('HomePage:up-per',kwargs={'user_id':self.user2.id})
        #Assert
        self.assertEqual(resolve(url).func.view_class, UpPermissions)


tag('unit-test')
class PostTestCase(TestCase):
    def setUp(self):
      self.credentials = {
            'title': 'TitleTest',
            'date': datetime.today(),
            'description': 'Testdescription'
      }
      self.post = Post.objects.create(**self.credentials)
  

    def test_title(self):
      self.assertEqual(self.post.title, 'TitleTest')
    
    def test_date(self):
      self.date = datetime.today()
      self.post.date = self.date
      self.assertEqual(self.post.date, self.date)
    
    def test_description(self):
      self.assertEqual(self.post.description, 'Testdescription')

