from odoo import models, fields

class Movie(models.Model):
    _name = 'movie'
    _description = 'Movie'

    name = fields.Char(string='Name', required=True)
    premiere = fields.Date(string='Premiere')
    category = fields.Selection([
        ('action', 'Action'),
        ('horror', 'Horror'),
        ('romance', 'Romance'),
        ('drama', 'Drama'),
        ('comedy', 'Comedy')
    ], string='Category')
    budget = fields.Float(string='Budget')
    image = fields.Binary(string='Image')
