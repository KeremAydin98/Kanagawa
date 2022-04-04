from django.test import TestCase
from django.urls import reverse

class HomePageTests(TestCase):

    def setUp(self):

        self.response = self.client.get(reverse('home'))

    def test_status_code(self):

        self.assertEqual(self.response.status_code, 200)

    def test_template_used(self):

        self.assertTemplateUsed(self.response, 'home.html')

    def test_contain(self):

        self.assertContains(self.response, 'HomePage')
