from django.urls import reverse
from rest_framework.test import APITestCase


# Create your tests here.

class UserTest(APITestCase):
    def setUp(self) -> None:
        self.username = 'testing1'
        self.password = 'testing200'
        self.fake_password = 'kolework'
        self.email = 'testing1@test.com'
        self.first_name = 'Testing'
        self.last_name = 'Last'
        self.fake_token = '<hisdsdGGGS74882826stssrssuwAWAwq**Ü*SS)W)'

    def register(self):
        resp = self.client.post(reverse('rest_register'),
                                {'username': self.username, 'password1': self.password, 'first_name': self.first_name,
                                 'password2': self.password, 'last_name': self.last_name, 'email': self.email})
        return resp

    def test_refresh_token(self):
        resp = self.client.post(reverse('refresh-token'), {'token': self.fake_token})
        self.assertEqual(resp.status_code, 400)

        token = self.register().json()['token']
        resp = self.client.post(reverse('refresh-token'), {'token': token})
        self.assertEqual(resp.status_code, 200)

    def test_verify(self):
        resp = self.client.post(reverse('verify-token'), {'token': self.fake_token})
        self.assertEqual(resp.status_code, 400)

        token = self.register().json()['token']
        verify_token = self.client.post(reverse('verify-token'), {'token': token})
        self.assertEqual(verify_token.status_code, 200)

    def test_login(self):
        self.register()
        resp = self.client.post(reverse('rest_login'), {'username': self.username, 'password': self.password})
        self.assertEqual(resp.status_code, 200)

        resp = self.client.post(reverse('rest_login'), {'username': self.username, 'password': self.fake_password})
        self.assertEqual(resp.status_code, 400)
