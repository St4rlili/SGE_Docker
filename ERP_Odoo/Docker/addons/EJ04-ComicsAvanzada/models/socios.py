from odoo import models, fields

class Socio(models.Model):
    _name = 'biblioteca.comic.socio'
    _description = 'Socio de la biblioteca'
    _rec_name = 'nombre'

    nombre = fields.Char(
        string='Nombre',
        required=True,
        help='Nombre del socio'
    )

    apellido = fields.Char(
    string='Apellido',
    required=True,
    help='Apellido del socio'
    )

    identificador = fields.Text(
        string='Identificador',
        required=True,
    )

    _sql_constraints = [
        ('identificador_unique', 'unique(identificador)', 'El identificador debe ser único')
    ]