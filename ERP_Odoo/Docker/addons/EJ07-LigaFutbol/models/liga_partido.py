# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError

class LigaPartido(models.Model):
    _name = 'liga.partido'
    _description = 'Un partido de la liga'

    equipo_casa = fields.Many2one('liga.equipo', string='Equipo local')
    goles_casa = fields.Integer()
    equipo_fuera = fields.Many2one('liga.equipo', string='Equipo visitante')
    goles_fuera = fields.Integer()

    # Actualiza los registros de los equipos según los resultados de los partidos
    def actualizoRegistrosEquipo(self):
        # Reiniciar todos los equipos
        for recordEquipo in self.env['liga.equipo'].search([]):
            recordEquipo.victorias = 0
            recordEquipo.empates = 0
            recordEquipo.derrotas = 0
            recordEquipo.goles_a_favor = 0
            recordEquipo.goles_en_contra = 0
            recordEquipo.puntos = 0

        # Recorrer todos los partidos y recalcular
        for partido in self.env['liga.partido'].search([]):
            local = partido.equipo_casa
            visitante = partido.equipo_fuera
            if not local or not visitante:
                continue

            goles_local = partido.goles_casa
            goles_vis = partido.goles_fuera
            diferencia = abs(goles_local - goles_vis)

            # Resultado
            if goles_local > goles_vis:
                # Regla de puntuación especial
                if diferencia >= 4:
                    local.puntos += 4
                    visitante.puntos = max(0, visitante.puntos - 1)
                else:
                    local.puntos += 3
                local.victorias += 1
                visitante.derrotas += 1

            elif goles_local < goles_vis:
                if diferencia >= 4:
                    visitante.puntos += 4
                    local.puntos = max(0, local.puntos - 1)
                else:
                    visitante.puntos += 3
                visitante.victorias += 1
                local.derrotas += 1

            else:  # Empate
                local.empates += 1
                visitante.empates += 1
                local.puntos += 1
                visitante.puntos += 1

            # Goles a favor y en contra
            local.goles_a_favor += goles_local
            local.goles_en_contra += goles_vis
            visitante.goles_a_favor += goles_vis
            visitante.goles_en_contra += goles_local

    # Botones para sumar goles
    def sumar_goles_locales(self):
        for partido in self.env['liga.partido'].search([]):
            partido.goles_casa += 2
        self.actualizoRegistrosEquipo()

    def sumar_goles_visitantes(self):
        for partido in self.env['liga.partido'].search([]):
            partido.goles_fuera += 2
        self.actualizoRegistrosEquipo()

    # Disparadores para actualizar al cambiar valores
    @api.onchange('equipo_casa', 'goles_casa', 'equipo_fuera', 'goles_fuera')
    def actualizar(self):
        self.actualizoRegistrosEquipo()

    def unlink(self):
        result = super(LigaPartido, self).unlink()
        self.actualizoRegistrosEquipo()
        return result

    @api.model
    def create(self, values):
        result = super().create(values)
        self.actualizoRegistrosEquipo()
        return result
    
    def print_report(self):
        """Genera el PDF del partido y lo devuelve para descargar"""
        return self.env.ref('EJ07-LigaFutbol.action_report_partido').report_action(self)

