from odoo import models, fields

class Ciclo(models.Model):
    _name = 'instituto.ciclo'
    _description = 'Ciclos Formativos'

    name = fields.Char(string='Nombre del Ciclo',required=True)
    modulo_ids = fields.One2many('instituto.modulo','ciclo_id',string='Módulos')