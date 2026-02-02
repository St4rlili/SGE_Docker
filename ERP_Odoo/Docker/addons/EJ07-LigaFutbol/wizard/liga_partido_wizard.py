# -*- coding: utf-8 -*-
from odoo import models, fields, api

class LigaPartidoWizard(models.TransientModel):
    _name = 'wizard.liga.partido'
    _description = 'Wizard para crear un nuevo partido'

    equipo_casa = fields.Many2one('liga.equipo', string='Equipo Local', required=True)
    goles_casa = fields.Integer(string='Goles Local', default=0)
    equipo_fuera = fields.Many2one('liga.equipo', string='Equipo Visitante', required=True)
    goles_fuera = fields.Integer(string='Goles Visitante', default=0)
    jornada = fields.Integer(string='Jornada', required=True)

    def crear_partido(self):
        """Crea un nuevo partido y actualiza la clasificación automáticamente"""
        self.env['liga.partido'].create({
            'equipo_casa': self.equipo_casa.id,
            'goles_casa': self.goles_casa,
            'equipo_fuera': self.equipo_fuera.id,
            'goles_fuera': self.goles_fuera,
        })
        return {'type': 'ir.actions.act_window_close'}
