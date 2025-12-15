from odoo import models, fields

class Alumno(models.Model):
    _name = 'instituto.alumno'
    _description = 'Alumno'

    name = fields.Char(string='Nombre del Alumno',required=True)
    modulo_ids = fields.Many2many('instituto.modulo', string='Módulos del Alumno')