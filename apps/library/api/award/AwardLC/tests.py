from rest_framework.test import APITestCase

from datetime import datetime
from django.shortcuts import reverse

from apps.library.models import Award
from apps.user.models import User


class AwardLCViewTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(email="test@gmail.com", password="123")
        self.client.force_login(self.user)
        self.award = Award.objects.create(name="Test Award", date=datetime.now().date())
        self.url = reverse("library:award_lc")

    def test_award_create_view(self):
        data = {"name": "Test Award", "date": datetime.now().date()}
        response = self.client.post(self.url, data, format="json")
        print(response.json())
        print(response.status_code)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json()["name"], "Test Award")

    def test_award_list_create_view(self):
        response = self.client.get(self.url)
        print(response.json())
        print(response.status_code)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()[0]["name"], "Test Award")
        