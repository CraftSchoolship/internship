from odoo import http
from odoo.http import request

class Main(http.Controller):
     @http.route('/movies', type='http', auth='public', website=True)
     def index(self, **kw):
          movies = request.env['internship.movie'].search([])
          vals = {
               'movies': movies
          }
          return request.render('internship.index', vals)