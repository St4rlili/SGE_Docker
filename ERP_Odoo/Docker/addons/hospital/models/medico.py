from odoo import models, fields

class Medico(models.Model):
    _name = 'hospital.medico'
    _description = 'Médico'

    name = fields.Char(string="Nombre y apellidos", required=True)
    numero_colegiado = fields.Char(string="Número de colegiado", required=True)

    consulta_ids = fields.One2many(
        'hospital.consulta',
        'medico_id',
        string="Consultas"
    )