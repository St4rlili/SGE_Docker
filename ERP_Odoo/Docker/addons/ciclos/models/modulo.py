from odoo import models, fields

class Modulo(models.Model):
    _name = 'instituto.modulo'
    _description = 'Módulo'

    name = fields.Char(string='Nombre del Módulo', required=True)
    ciclo_id = fields.Many2one('instituto.ciclo', string='Ciclo Formativo', required=True)
    alumnos_ids = fields.Many2many('instituto.alumno', string='Alumnos Matriculados')
    profesor_id = fields.Many2one('instituto.profesor', string='Profesor')