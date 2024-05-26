import unittest
from app import app

class APITestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_get_songs(self):
        response = self.app.get('/songs?page=1&per_page=2')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(response.json) <= 2)

    def test_get_song_by_title(self):
        response = self.app.get('/song/3AM')
        self.assertEqual(response.status_code, 200)
        self.assertIn('title', response.json)
        self.assertEqual(response.json['title'], '3AM')

    def test_rate_song(self):
        response = self.app.post('/song/3AM/rate', json={'rating': 5})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['message'], 'Rating updated')

if __name__ == '__main__':
    unittest.main()

