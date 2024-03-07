from odoo import models, fields

class Movie(models.Model):
    _name = 'model.movie'
    # _inherit = 'mail.thread'
    _description = "Movie"
    Name = fields.Char(string='Name')
    Premiere = fields.Date(string='Premiere')
    Category = fields.Selection([('action', 'Action'), ('horror', 'Horror'), ('romance', 'Romance'), ('drama', 'Drama'), ('comedy', 'Comedy')],
                                string='Category')
    Budget = fields.Float(string='Budget')
    # Image = fields.Binary(string='Image', attachment=True)