from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework.reverse import reverse
from django.contrib.auth import get_user_model

from .tokens import jwt_payload_handler, jwt_encode_handler


User = get_user_model()


def create_test_user():
    return User.objects.create_user(email="test@test.pl",
                                    username="test",
                                    password="password")


class CreateUserTest(APITestCase):
    """Ensure we can create a new user."""

    def setUp(self):
        self.url = reverse('register')

    def test_create_user(self):

        data = {"email": "test@test.pl", "username": "test", "password": "password"}

        response = self.client.post(self.url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().username, 'test')
        self.assertTrue("token" in response.data)

    def test_create_user_missing_data(self):

        data = {"email": "test@test.pl", "password": "password"}

        response = self.client.post(self.url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(User.objects.count(), 0)
        self.assertTrue("token" not in response.data)


class LoginTest(APITestCase):
    """Test login"""

    def setUp(self):

        # First create a test user

        create_test_user()

        # Set the url for login endpoint

        self.url = reverse('login')

    def test_login(self):
        """ Test for obtaining JWT token"""

        data = {"email": "test@test.pl", "password": "password"}

        response = self.client.post(self.url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue("token" in response.data)

    def test_login_username(self):
        """ Test for obtaining JWT token with username instead of password"""

        data = {"username": "test", "password": "password"}

        response = self.client.post(self.url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertTrue("token" not in response.data)

    def test_login_fake_credentials(self):
        """ Test for obtaining JWT token with bogus credentials"""

        data = {"email": "fake@user.account", "password": "Iisgonnagetin"}

        response = self.client.post(self.url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertTrue("token" not in response.data)


class JWTTokenTest(APITestCase):
    """Test for login with JWT token"""

    def setUp(self):

        # First create a test user

        user = create_test_user()

        # Get JWT token

        payload = jwt_payload_handler(user)
        self.token = jwt_encode_handler(payload)

        # Set the url for users endpoint

        self.url = reverse('users')

    def test_access_to_protected_resource(self):
        """ Test for accessing a protected resource"""

        # Add the token to the requests' headers
        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + self.token)
        response = self.client.get(self.url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_access_to_protected_resource_without_credentials(self):
        """ Test for accessing a protected resource without credentials"""

        response = self.client.get(self.url, format='json)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
