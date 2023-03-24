from django.test import TestCase, Client
from django.urls import reverse
from subscriptions_rest.models import User

# Tests by Adrian and Morgan
class TestViews(TestCase):
        
    def test_login_works(self):
        User.objects.create_user("nerd", password="password1234")
        response = self.client.post(
            reverse("login"),
            {"username": "nerd", "password": "password1234"},
        )
        self.assertEqual(
            response.status_code,
            200,
            msg="Login not working",
        )