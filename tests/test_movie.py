from odoo.tests.common import TransactionCase
from datetime import datetime
from odoo.exceptions import ValidationError

class TestMovieCreation(TransactionCase):
    
    def test_movie_creation(self):
        # Récupération du modèle Movie
        Movie = self.env['internship.movie']

        # Data movie
        movie_data = {
            'name': "Inception",
            'premiere': datetime.today().date(),
            'category': 'romance',
            'budget': 540000000,
            'image': b'my_binary_image_data'
        }

        # Movie creation test with valid data
        movie = Movie.create(movie_data)
        self.assertEqual(movie.name, "Inception")

        
        # Required fields validation test
        with self.assertRaises(ValidationError):
            Movie.create({'name': 'Test Movie'})

        # Category field validation test
        with self.assertRaises(ValidationError):
            movie_data['category'] = 'invalid_category'
            Movie.create(movie_data)

        # Test de validation du champ de budget négatif
        # Negative budget field validation test
        with self.assertRaises(ValidationError):
            movie_data['category'] = 'romance'
            movie_data['budget'] = -200
            Movie.create(movie_data)
