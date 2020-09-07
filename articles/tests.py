from django.test import TestCase, SimpleTestCase, Client
from django.urls import reverse_lazy, reverse
from django.contrib.auth import get_user_model
from .models import Article

class ArticleListTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username="test", password="password", email="test@email.com")
        self.client.force_login(get_user_model().objects.get_or_create(username=self.user.username)[0])

    def test_status_code(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_view_by_name(self):
        response = self.client.get(reverse_lazy("article_list"))
        self.assertEqual(response.status_code, 200)


    def test_template(self):
        response = self.client.get(reverse_lazy("article_list"))
        self.assertTemplateUsed("article_list.html")


class ArticleCreateTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username="test", password="password", email="test@email.com")
        self.client.force_login(get_user_model().objects.get_or_create(username=self.user.username)[0])


    def test_template(self):
        response = self.client.get(reverse_lazy("create_article"))
        self.assertTemplateUsed("articles/create_article.html")


    def test_view_by_name(self):
        response = self.client.get(reverse_lazy("create_article"))
        self.assertEqual(response.status_code, 200)

    def test_article_creation(self):
        response = self.client.post(reverse("create_article"), dict(title="test", body="test body", author=self.user))
        self.assertEqual(response.status_code, 302)


class ArticleDetailTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(email='test@email.com', password="password", username='test')
        self.article = Article.objects.create(title="test title", body="test body", author=self.user)
        self.client.force_login(get_user_model().objects.get_or_create(username=self.user.username)[0])

    def test_article_detail_status_code(self):
        response = self.client.get(reverse_lazy("article_detail", args=str(self.article.id),))
        self.assertEqual(response.status_code, 200)

    def test_article_detail_template(self):
        response = self.client.get(reverse_lazy("article_detail", args=str(self.article.id),))
        self.assertTemplateUsed(response, "articles/article_detail.html")


class ArticleUpdateTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(email='test@mail.com', username='test', password="password")
        self.article = Article.objects.create(title="test title", body="test body", author=self.user)
        self.client.force_login(get_user_model().objects.get_or_create(username=self.user.username)[0])

    def test_article_update_status(self):
        response = self.client.post(reverse_lazy("article_edit", args=str(self.article.id),), kwargs=dict(title="[UPDATE:] Title updated", body="Body text", author=self.user))
        self.assertEqual(response.status_code, 200)
