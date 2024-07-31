from datetime import datetime

from django.shortcuts import reverse
from rest_framework.test import APITestCase

from apps.library.models import Award
from apps.user.models import User


class AwardRetrieveViewTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(email="test@gmail.com", password="123")
        self.client.force_login(self.user)
        self.award = Award.objects.create(name="Test Award", date=datetime.now().date())
        self.url = reverse("library:award_rud", kwargs={"pk": self.award.pk})

    def test_retrieve_award(self):
        response = self.client.get(self.url)
        print(response.json())
        print(response.status_code)
        self.assertEqual(response.status_code, 200)
        