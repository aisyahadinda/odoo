from odoo import models, fields

class BirthCity(models.Model):
    _name = "latihan.birthcity"

    name = fields.Char(string="Nama Kota", required=True)
