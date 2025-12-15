from odoo import models, fields

class Profesor(models.Model):
    _name = 'instituto.profesor'
    _description = 'Profesor'

    name = fields.Char(string='Nombre del Profesor',required=True)
    modulo_ids = fields.Many2many('instituto.modulo', string='Módulos del Profesor')