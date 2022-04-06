from django.test import TestCase
from django.urls import reverse
from .models import Book, Comment
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission


class BookPageTests(TestCase):

    def setUp(self):

        self.user = get_user_model().objects.create_user(
            username = "Kero",
            email = 'keremtest@email.com',
            password='testpass123'
        )
        self.special_permission = Permission.objects.get(codename='special_status')

        self.book = Book.objects.create(
            title="Dune",
            author="Frank Herbert",
            price = 10.1,
        )

        self.comment = Comment.objects.create(
            book = self.book,
            author = self.user,
            comment = "excellent",
        )


    def test_book_listing(self):

        self.assertEqual(f"{self.book.title}", "Dune")
        self.assertEqual(f"{self.book.author}", "Frank Herbert")

    def test_book_list_page_logged_in(self):

        self.client.login(username="Kero", password="testpass123")

        response = self.client.get(reverse('book_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Dune")
        self.assertTemplateUsed(response, "books/book_list.html")

    def test_book_list_page_logged_out(self):

        self.client.logout()

        response = self.client.get(reverse('book_list'))

        self.assertEqual(response.status_code, 302)

        self.assertRedirects(
            response, '%s?next=/books/' % (reverse('account_login')))
        response = self.client.get(
            '%s?next=/books/' % (reverse('account_login')))
        self.assertContains(response, 'Log In')

    def test_book_detail_page_logged_in(self):

        self.client.login(username="Kero", password="testpass123")

        self.user.user_permissions.add(self.special_permission)

        response = self.client.get(self.book.get_absolute_url())
        no_response = self.client.get("/books/12345/")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, "Dune")
        self.assertContains(response, "excellent")
        self.assertTemplateUsed(response, "books/book_detail.html")