# -*- coding: utf-8 -*-
from odoo import models, fields, api
#Definimos el modelo de datos
class lista_tareas(models.Model):
#Nombre y descripcion del modelo de datos
    _name = 'lista_tareas.lista_tareas'
    _description = 'lista_tareas.lista_tareas'
#Elementos de cada fila del modelo de datos
#Los tipos de datos a usar en el ORM son
    tarea = fields.Char()
    prioridad = fields.Integer()
    urgente = fields.Boolean(compute="_value_urgente", store=True)
    realizada = fields.Boolean()
    fecha_creacion = fields.Datetime(string="Fecha de creación",default=fields.Datetime.now)
    fecha_terminada = fields.Datetime(string="Fecha de finalización",compute="_compute_fecha_terminada",store=True)

    @api.depends('prioridad')
    def _value_urgente(self):
        for record in self:
            if record.prioridad>10:
                record.urgente = True
            else:
                record.urgente = False

    @api.depends('realizada')
    def _compute_fecha_terminada(self):
        for record in self:
            if record.realizada and not record.fecha_terminada:
                record.fecha_terminada = fields.Datetime.now()
            else:
                record.fecha_terminada = False