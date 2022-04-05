from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

class CustomUserTests(TestCase):

    def setUp(self):

        User = get_user_model()

        self.user = User.objects.create_user(
            username = 'kerem',
            email = 'test@email.com',
            password = 'testpass123'
        )

        self.super_user = User.objects.create_superuser(
            username= 'superadmin',
            email ='supermanadmin@email.com',
            password ='testsuperuser123',
        )

    def test_custom_user(self):

        self.assertEqual(self.user.username, 'kerem')
        self.assertEqual(self.user.email, 'test@email.com')
        self.assertTrue(self.user.is_active)
        self.assertFalse(self.user.is_staff)
        self.assertFalse(self.user.is_superuser)

    def test_super_user(self):

        self.assertEqual(self.super_user.username, 'superadmin')
        self.assertEqual(self.super_user.email, 'supermanadmin@email.com')
        self.assertTrue(self.super_user.is_active)
        self.assertTrue(self.super_user.is_staff)
        self.assertTrue(self.super_user.is_superuser)

class SignUpPageTests(TestCase):

    username = 'test123'
    email = 'testuser@email.com'

    def setUp(self):

        self.response = self.client.get(reverse('account_signup'))

    def test_signup_status_code(self):

        self.assertEqual(self.response.status_code, 200)

    def test_signup_template_used(self):

        self.assertTemplateUsed(self.response, 'account/signup.html')

    def test_signup_contains(self):

        self.assertContains(self.response, 'Sign Up')