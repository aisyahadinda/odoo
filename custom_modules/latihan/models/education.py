from odoo import models, fields

class Education(models.Model):
    _name = 'latihan.education'
    _description = 'Pendidikan'

    name = fields.Char(string='Nama Pendidikan', required=True)
