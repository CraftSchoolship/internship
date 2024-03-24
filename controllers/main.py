import prometheus_client
from odoo import http
from odoo.http import request, Response

class Main(http.Controller):
    @http.route('/movies', type='http', auth='public', website=True)
    def home_index(self, **kw):        
        movies = request.env['internship.movie'].search([])
        values = {
            'movies': movies
        }
        return request.render('internship.index', values)
    
    @http.route('/prometheus/metrics', type='http', auth='public')
    def prometheus_metrics(self):
        registry = prometheus_client.CollectorRegistry(auto_describe=True)
        metrics = prometheus_client.generate_latest(registry)
        return Response(metrics, content_type='text/plain; version=0.0.4')
