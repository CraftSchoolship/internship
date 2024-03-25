from odoo import models, fields
from prometheus_client import Counter, Histogram
import time

class Movie(models.Model):
    _name = 'internship.movie'
    _description = 'Movie Model'

    name = fields.Char(string='Name', required=True)
    premiere = fields.Date(string='Premiere')
    category = fields.Selection([('action', 'Action'), ('horror', 'Horror'), ('romance', 'Romance'), ('drama', 'Drama'), ('comedy', 'Comedy')],
                                string='Category')
    budget = fields.Float(string='Budget')
    image = fields.Binary(string='Image', attachment=True)

    # Initialisation des métriques spécifiques à la classe Movie
    movie_counter = Counter('odoo_movie_added_total', 'Total number of movies added')
    movie_duration_histogram = Histogram('odoo_movie_add_duration_seconds', 'Duration of adding a movie in seconds')

    def add_movie(self):
        start_time = time.time()

        # Logique pour ajouter un film...

        end_time = time.time()

        # Incrémenter le compteur de films ajoutés
        self.movie_counter.inc()

        # Observer la durée de l'ajout du film
        self.movie_duration_histogram.observe(end_time - start_time)
