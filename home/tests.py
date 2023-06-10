from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.test.client import Client

from home.models import TextAnalysisResult


class TextAnalysisTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser', password='testpassword')

    def test_summarize_view(self):
        self.client.login(username='testuser', password='testpassword')

        form_data = {'text': 'This is a test text.'}

        response = self.client.post(reverse('summarize'), data=form_data)

        self.assertEqual(response.status_code, 200)

        self.assertEqual(TextAnalysisResult.objects.count(), 1)

    def test_stemmer_view(self):
        self.client.login(username='testuser', password='testpassword')

        form_data = {'text': 'This is a test text.'}

        response = self.client.post(reverse('stemmer'), data=form_data)

        self.assertEqual(response.status_code, 200)

        self.assertEqual(TextAnalysisResult.objects.count(), 1)

    def test_lemmatizer_view(self):
        self.client.login(username='testuser', password='testpassword')

        form_data = {'text': 'This is a test text.'}

        response = self.client.post(reverse('lemmatizer'), data=form_data)

        self.assertEqual(response.status_code, 200)

        self.assertEqual(TextAnalysisResult.objects.count(), 1)

    def test_stopwordremove_view(self):
        self.client.login(username='testuser', password='testpassword')

        form_data = {'text': 'This is a test text.'}

        response = self.client.post(reverse('stopwordremove'), data=form_data)

        self.assertEqual(response.status_code, 200)

        self.assertEqual(TextAnalysisResult.objects.count(), 1)

    def test_textclass_view(self):
        self.client.login(username='testuser', password='testpassword')

        form_data = {'text': 'This is a test text.'}

        response = self.client.post(reverse('textclass'), data=form_data)

        self.assertEqual(response.status_code, 200)

        self.assertEqual(TextAnalysisResult.objects.count(), 1)
