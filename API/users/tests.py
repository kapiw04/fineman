from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status
from django.contrib.auth.models import User
# TODO: remove below lines
# check if the algo used is in fact rsa512

# Create your tests here.
client = Client()

class JwtTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user("filip",password="kochamsiostre123")
        self.user.save()

    def test_rsa(self):
        """Check is RSA is enabled"""
        from django.conf import settings
        self.assertEqual(settings.SIMPLE_JWT["ALGORITHM"], "RS512")  

    def test_generate_jwt(self):
        body = {"username": "filip", "password": "kochamsiostre123"}
        response = client.post(reverse('token_obtain_pair'), data=body,  format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertNotEqual(response.data['access'], "")
        self.assertNotEqual(response.data['refresh'], "")

    def test_generate_jwt_negative(self):
        body = {"username": "bezimienny", "password": "kochamsiostre123"}
        response = client.post(reverse('token_obtain_pair'), data=body,  format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_claims_authentication(self):
        body = {"username": "filip", "password": "kochamsiostre123"}
        response = client.post(reverse('token_obtain_pair'), data=body,  format='json')
        headers = {"Authorization": "Bearer " + response.data['access']}
        verified_view = client.get(reverse('test_jwt_auth'), headers=headers)
        self.assertEqual(verified_view.status_code, status.HTTP_200_OK)

    def test_claims_authentication_negative(self):
        headers = {"Authorization": "Bearer " + "invalid token"}
        verified_view = client.get(reverse('test_jwt_auth'), headers=headers)
        self.assertEqual(verified_view.status_code, status.HTTP_401_UNAUTHORIZED)
