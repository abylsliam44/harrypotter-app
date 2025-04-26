from django.test import TestCase, Client
from django.urls import reverse
from unittest.mock import patch
from slugify import slugify

class HogwartsViewsTests(TestCase):
    def setUp(self):
        # Initialize test client
        self.client = Client()

    def test_home_view(self):
        # Test home page loads successfully
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'hogwarts/home.html')

    def test_houses_view(self):
        # Test houses page loads successfully
        response = self.client.get(reverse('houses'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'hogwarts/houses.html')

    @patch('hogwarts.views.requests.get')
    def test_characters_view(self, mock_get):
        # Mock external API call and test characters list page
        mock_get.return_value.json.return_value = [
            {"name": "Harry Potter", "house": "Gryffindor"}
        ]
        response = self.client.get(reverse('characters'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'hogwarts/characters.html')
        self.assertIn('page_obj', response.context)

    @patch('hogwarts.views.requests.get')
    def test_character_detail_view_valid(self, mock_get):
        # Test character detail view with a valid slug
        mock_get.return_value.json.return_value = [
            {"name": "Harry Potter", "house": "Gryffindor"}
        ]
        slug = slugify("Harry Potter")
        response = self.client.get(reverse('character_detail', args=[slug]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'hogwarts/character_detail.html')

    @patch('hogwarts.views.requests.get')
    def test_character_detail_view_invalid(self, mock_get):
        # Test character detail view with an invalid slug
        mock_get.return_value.json.return_value = [
            {"name": "Harry Potter"}
        ]
        response = self.client.get(reverse('character_detail', args=['nonexistent-character']))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'hogwarts/character_not_found.html')

    def test_favorites_view(self):
        # Test favorites page loads successfully
        response = self.client.get(reverse('favorites'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'hogwarts/favorites.html')

    @patch('hogwarts.views.requests.post')
    def test_chat_with_character_get(self, mock_post):
        # Test chat page (GET method)
        response = self.client.get(reverse('chat_with_character', args=[slugify('Harry Potter')]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'hogwarts/chat.html')

    @patch('hogwarts.views.requests.post')
    def test_chat_with_character_post(self, mock_post):
        # Test chat API interaction (POST method)
        mock_post.return_value.json.return_value = [{
            "generated_text": "Harry Potter: Hello there!"
        }]
        response = self.client.post(reverse('chat_with_character', args=[slugify('Harry Potter')]), {
            'message': 'Hello!'
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn('application/json', response['Content-Type'])

    @patch('hogwarts.views.requests.get')
    def test_quiz_view_get(self, mock_get):
        # Test quiz page (GET method)
        mock_get.return_value.json.return_value = {
            "results": [
                {
                    "question": "Who is Harry Potter?",
                    "correct_answer": "The Boy Who Lived",
                    "incorrect_answers": ["A teacher", "A villain", "A ghost"]
                }
            ] * 5
        }
        response = self.client.get(reverse('quiz'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'hogwarts/quiz.html')
        self.assertIn('questions', response.context)

    @patch('hogwarts.views.requests.get')
    def test_quiz_view_post(self, mock_get):
        # Test quiz submission and scoring (POST method)
        mock_get.return_value.json.return_value = {
            "results": [
                {
                    "question": "Who is Harry Potter?",
                    "correct_answer": "The Boy Who Lived",
                    "incorrect_answers": ["A teacher", "A villain", "A ghost"]
                }
            ] * 5
        }
        post_data = {
            'q1': 'The Boy Who Lived',
            'q2': 'The Boy Who Lived',
            'q3': 'The Boy Who Lived',
            'q4': 'The Boy Who Lived',
            'q5': 'The Boy Who Lived',
        }
        response = self.client.post(reverse('quiz'), data=post_data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'hogwarts/quiz_result.html')
        self.assertIn('score', response.context)
