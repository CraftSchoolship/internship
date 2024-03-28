import time  
import prometheus_client
from odoo import http
from odoo.http import request, Response

# Créer un compteur pour les films
movies_counter = prometheus_client.Counter('odoo_movies_total', 'Total number of movies')

# Créer un histogramme pour enregistrer la durée des requêtes en secondes
request_duration_histogram = prometheus_client.Histogram(
    'odoo_http_request_duration_seconds',
    'Histogram for the duration of requests in seconds.',
    buckets=(1, 2, 5, 6, 10, float('inf'))  # Définir les buckets en secondes
)

class Main(http.Controller):

    @http.route('/movies', type='http', auth='public', website=True)
    def home_index(self, **kw):  
        # Début de la mesure du temps de la requête
        start_time = time.time()      
        movies = request.env['internship.movie'].search([])
        values = {
            'movies': movies
        }
        # Fin de la mesure du temps de la requête
        end_time = time.time()

        # Incrémenter le compteur de films
        movies_counter.inc(len(movies))
        
        # Observer la durée de la requête
        request_duration_histogram.observe(end_time - start_time)
        
        return request.render('internship.index', values)
    
    @http.route('/prometheus/metrics', type='http', auth='public')
    def prometheus_metrics(self):
        # Récupérer les métriques du compteur de films
        movies_metrics = prometheus_client.generate_latest(movies_counter)
        # Récupérer les métriques de l'histogramme de la durée des requêtes
        request_duration_metrics = prometheus_client.generate_latest(request_duration_histogram)
        # Concaténer les métriques
        metrics = movies_metrics + request_duration_metrics
        return Response(metrics, mimetype='text/plain')
