from odoo import models, fields
import prometheus_client
from prometheus_client.core import CollectorRegistry
from prometheus_client import Summary, Counter, Histogram, Gauge

# Définir un compteur pour suivre le nombre total de films créés
movie_counter = Counter('odoo_movies_created_total', 'Total number of movies created')

# Définir un histogramme pour suivre la durée des opérations de création de film
movie_creation_duration = Histogram('odoo_movie_creation_duration_seconds', 'Duration of movie creation operations')


class Movie(models.Model):
    _name = 'internship.movie'
    _description = 'Movie Model'

    name = fields.Char(string='Name', required=True)
    premiere = fields.Date(string='Premiere')
    category = fields.Selection([('action', 'Action'), ('horror', 'Horror'), ('romance', 'Romance'), ('drama', 'Drama'), ('comedy', 'Comedy')],
                                string='Category')
    budget = fields.Float(string='Budget')
    image = fields.Binary(string='Image', attachment=True)

    def create(self, vals):
        start_time = time.time()
        result = super(Movie, self).create(vals)
        duration = time.time() - start_time
        movie_counter.inc()
        movie_creation_duration.observe(duration)
        return result


  