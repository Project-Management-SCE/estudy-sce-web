from django.test import TestCase, tag
from django.urls import reverse,resolve
from YouTube.views import SearchVideoView
# Create your tests here.

@tag('y')
class YouTubeTest(TestCase):

  def test_url(self):
    url = reverse("YouTube:youtube")
    self.assertEqual(resolve(url).func.view_class, SearchVideoView)

  def test_get(self):
    response = self.client.get(reverse("YouTube:youtube"))
    self.assertEqual(response.status_code, 200)


  def test_post(self):
    search = "c++"
    response = self.client.post(reverse("YouTube:youtube"),data={'search':search})
    self.assertEqual(response.status_code, 200)

  def test_post_return(self):
    search = "python"
    response = self.client.post(reverse("YouTube:youtube"),data={'search':search})
    self.assertNotEquals(response.context['videos'],None)
