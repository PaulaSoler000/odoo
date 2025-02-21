from odoo import models, fields, api

class LibraryBook(models.Model):
    _name = 'library.book'
    _description = 'Libro'

    title = fields.Char(string='Título', required=True)
    publication_date = fields.Date(string='Fecha de publicación')
    author_id = fields.Many2one('library.author', string='Autor', required=True)
