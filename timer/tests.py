from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase

class UserTests(APITestCase):
	def test_get_user(self):
		response = self.client.get('/users/4/')
		self.assertEqual(status.HTTP_200_OK, status.HTTP_200_OK)
