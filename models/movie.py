from odoo import api , fields, models

class Movie(models.Model):
    _name = "Movie.movie"
    _description = "Movie"
    name = fields.Char(string='Name', required=True)
    premiere = fields.Date(string='Premiere Date')
    category = fields.Selection([
        ('action', 'Action'),
        ('horror', 'Horror'),
        ('romance', 'Romance'),
        ('drama', 'Drama'),
        ('comedy', 'Comedy')
    ], string='Category')
    budget = fields.Float(string='Budget')
    image = fields.Binary(string='Image')