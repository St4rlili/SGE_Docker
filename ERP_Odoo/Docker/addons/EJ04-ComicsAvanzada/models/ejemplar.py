from odoo import models,fields, api
from odoo.exceptions import ValidationError
from datetime import date

class ComicEjemplar(models.Model):
    _name = 'biblioteca.comic.ejemplar'
    _description = 'Ejemplar de cómic'

    nombre = fields.Char(
        string='Nombre',
        related='comic_id.nombre',
        readonly=True
    )
    comic_id = fields.Many2one(
        'biblioteca.comic',
        string='Cómic',
        required=True
    )
    socio_id = fields.Many2one(
        'biblioteca.comic.socio',
        string='Prestado a'
    )
    fecha_prestamo = fields.Date(
        string='Fecha de préstamo'
    )
    fecha_devolucion = fields.Date(
        string='Fecha prevista de devolución'
    )
    estado = fields.Selection(
        [('disponible', 'Disponible'), ('prestado', 'Prestado')],
        string='Estado',
        compute='_compute_estado',
        store=True
    )

    @api.constrains('fecha_prestamo')
    def _check_fecha_prestamo(self):
        for record in self:
            if record.fecha_prestamo and record.fecha_prestamo > date.today():
                raise ValidationError('La fecha de préstamo no puede ser posterior al día actual')
    
    @api.constrains('fecha_devolucion')
    def _check_fecha_devolucion(self):
        for record in self:
            if record.fecha_devolucion and record.fecha_devolucion < date.today():
                raise ValidationError('La fecha prevista de devolución no puede ser anterior al día actual')
            
    @api.depends('socio_id', 'fecha_prestamo')
    def _compute_estado(self):
        for record in self:
            if record.socio_id and record.fecha_prestamo:
                record.estado = 'prestado'
            else:
                record.estado = 'disponible'