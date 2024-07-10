from odoo import models, fields

class Address(models.Model):
    _name = "latihan.address"
    _description = "Alamat"

    street = fields.Char(string="Jalan")
    city = fields.Char(string="Kota")
    state = fields.Char(string="Provinsi")
    zip = fields.Char(string="Kode Pos")
    country_id = fields.Many2one('res.country', string="Negara")
    biodata_id = fields.Many2one('latihan.biodata', string="Biodata")
