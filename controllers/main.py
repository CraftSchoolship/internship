from odoo import http
from odoo.http import request


class Main(http.Controller):
     @http.route('/movies', type='http', auth='public', website=True)
     def home_index(self, **kw):        
          movies = request.env['internship.movie'].search([])
          values = {
               'movies': movies
          }
          return request.render('internship.index', values)