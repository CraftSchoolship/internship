from odoo.tests.common import TransactionCase
from odoo.exceptions import ValidationError
from datetime import datetime

class TestMoieModel(TransactionCase):

    def test_movie_creation(self):
        Movie =  self.env['intership.movie']
        movie_data = {
            'name':"Inception",
            'premiere':datetime.today().date(),
            'category': 'action',
            'budget': 200000000,
            'image': b'my_binary_image_data' 
        }

        # Test de création de film avec des données valides
        movie = Movie.create(movie_data)
        self.assertEqual(movie.name, "Inception")

        # Test de validation des champs obligatoires
        with self.assertRaises(ValidationError):
            movie.create({'name': 'Test Movie'})

        # test de validtaion du cahp de catégorie
        with self.assertRaises(ValidationError):
            movie_data['category'] = 'invalid_category'
            movie.create(movie_data)

        #Test de validation du champ de budget négatif 
            movie_data['category']= 'action'
            movie_data['budget']= -100
            movie.create(movie_data)   