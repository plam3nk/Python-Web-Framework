from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

UserModel = get_user_model()


class LoginUserViewTest(TestCase):
    def test_login_user(self):
        user_data = {
            'username': 'plamen',
            'password': '1q2w3e@ASDASLIU8$!@#',
        }

        UserModel.objects.create_user(**user_data)
        self.client.login(**user_data)

        response = self.client.get(reverse('index'))

