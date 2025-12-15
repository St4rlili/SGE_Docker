from odoo import models, fields

class Consulta(models.Model):
    _name = 'hospital.consulta'
    _description = 'Consulta Médica'

    paciente_id = fields.Many2one(
        'hospital.paciente',
        string="Paciente",
        required=True
    )

    medico_id = fields.Many2one(
        'hospital.medico',
        string="Médico",
        required=True
    )

    diagnostico = fields.Text(string="Diagnóstico")
    fecha = fields.Datetime(string="Fecha", default=fields.Datetime.now)