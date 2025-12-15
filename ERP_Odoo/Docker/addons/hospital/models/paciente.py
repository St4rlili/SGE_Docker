from odoo import models, fields

class Paciente(models.Model):
    _name = 'hospital.paciente'
    _description = 'Paciente'

    name = fields.Char(string="Nombre y apellidos",required=True)
    sintomas = fields.Text(string="Síntomas")

    consulta_ids = fields.One2many(
        'hospital.consulta',
        'paciente_id',
        string="Consultas"
    )