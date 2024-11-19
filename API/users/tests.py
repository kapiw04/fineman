from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status
from django.contrib.auth.models import User
# Create your tests here.
client = Client()

class JwtTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user("filip",password="kochamsiostre123")
        self.user.save()

    def test_generate_jwt(self):
        body = {"username": "filip", "password": "kochamsiostre123"}
        response = client.post(reverse('token_obtain_pair'), data=body,  format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertNotEqual(response.data['access'], "")
        self.assertNotEqual(response.data['refresh'], "")


