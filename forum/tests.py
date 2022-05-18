from datetime import datetime
from django.test import TestCase, tag
from django.urls import resolve, reverse
from forum.views import forumView
from forum.models import Post
from accounts.models import User

# Create your tests here.


@tag("unit-test")
class ForumPageTestCase(TestCase):
    def test_forumView(self):
        # Act
        url = reverse("Forum:forum-main")
        # Assert
        self.assertEqual(resolve(url).func.view_class, forumView)


@tag("unit-test")
class PostTestCase(TestCase):
    def setUp(self):
        self.credentials = {
            "username": "lectureruser",
            "password": "5t4r3e2w1q",
            "is_lecturer": True,
        }

        self.user_lecturer = User.objects.create(**self.credentials)

    def test_postView(self):
        # Act
        form = {"message": "contant!"}
        response = self.client.post(
            reverse("Forum:post-post", kwargs={"user_id": self.user_lecturer.id}),
            data=form,
            follow=True,
        )
        # Assert
        self.assertEqual(response.status_code, 200)
