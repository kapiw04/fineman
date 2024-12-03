from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status
from django.contrib.auth.models import User
import base64
import json

# Create your tests here.
client = Client()

class JwtTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user("filip",password="kochamsiostre123")
        self.user.save()

    def test_rsa(self):
        body = {"username": "filip", "password": "kochamsiostre123"}
        response = client.post(reverse('token_obtain_pair'), data=body,  format='json')
        fields = [base64.urlsafe_b64decode(x.encode() + b"==") for x in response.data['access'].split('.')]
        #print("Header: ", fields[0].decode())
        #print("Payload: ", fields[1].decode())
        self.assertEqual(json.loads(fields[0]), {'alg':'RS512', 'typ':"JWT"})


    def test_generate_jwt_when_user_exists(self):
        body = {"username": "filip", "password": "kochamsiostre123"}
        response = client.post(reverse('token_obtain_pair'), data=body,  format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertNotEqual(response.data['access'], "")
        self.assertNotEqual(response.data['refresh'], "")

    def test_generate_jwt_when_user_does_not_exist(self):
        body = {"username": "bezimienny", "password": "kochamsiostre123"}
        response = client.post(reverse('token_obtain_pair'), data=body,  format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_claims_authentication(self):
        body = {"username": "filip", "password": "kochamsiostre123"}
        response = client.post(reverse('token_obtain_pair'), data=body,  format='json')
        headers = {"Authorization": "Bearer " + response.data['access']}
        verified_view = client.get(reverse('test_jwt_auth'), headers=headers)
        self.assertEqual(verified_view.status_code, status.HTTP_200_OK)

    def test_jwt_authentication_given_non_jwt_token(self):
        headers = {"Authorization": "Bearer " + "invalid token"}
        verified_view = client.get(reverse('test_jwt_auth'), headers=headers)
        self.assertEqual(verified_view.status_code, status.HTTP_401_UNAUTHORIZED)
