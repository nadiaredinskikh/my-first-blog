from django.test import TestCase, Client
from blog.models import Post


class HomePageTest(TestCase):
	def test_homepage_available(self):
		c = Client()
		response = c.get('/')
		self.assertEquals(response.status_code, 200)
	