from django.test import TestCase
from .models import Post
from django.urls import reverse

class PostModelTest(TestCase):
    
    def setUp(self):
        self.post = Post.objects.create(title='Test Title', content='Test Content')

    def test_post_creation(self):
        self.assertEqual(self.post.title, 'Test Title')
        self.assertEqual(self.post.content, 'Test Content')

class PostViewTest(TestCase):
    
    def setUp(self):
        self.post = Post.objects.create(title='Test Title', content='Test Content')

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'blog/post_list.html')
