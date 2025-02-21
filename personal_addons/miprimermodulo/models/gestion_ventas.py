from odoo import models, fields, api

class GestionVentas(models.Model):
    _name = 'gestion.ventas'
    _description = 'Gestion Ventas'

    name = fields.Char(string='Nombre', required=True)
    fecha_compra = fields.Date(string='Fecha de Compra', required=True)
    descripcion = fields.Text(string='Descripción')
    activo = fields.Boolean(string='Activo', default=True)