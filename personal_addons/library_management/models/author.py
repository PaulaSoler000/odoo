from odoo import models, fields, api

class LibraryAuthor(models.Model):
    _name = 'library.author'
    _description = 'Autor de libros'

    name = fields.Char(string='Nombre', required=True)
    birthdate = fields.Date(string='Fecha de nacimiento')
    biography = fields.Text(string='Biografía')
    book_ids = fields.One2many('library.book', 'author_id', string='Libros')
