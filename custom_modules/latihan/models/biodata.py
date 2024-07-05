from odoo import models, fields

class Biodata(models.Model):
    _name = "latihan.biodata"

    name = fields.Char(string="Nama")
    fullname = fields.Char(string="Nama Lengkap")
    from odoo import models, fields

class Biodata(models.Model):
    _name = "latihan.biodata"

    name = fields.Char(string="Nama")
    fullname = fields.Char(string="Nama Lengkap")
    birth_date = fields.Date(string="Tanggal Lahir")
    age = fields.Integer(string="Umur")
    children = fields.Integer(string="Anak ke-")
    photo = fields.Image(string="Foto")
    gender = fields.Char(String="Jenis Kelamin")
    education = fields.Selection([
        ('sd', 'SD'),
        ('smp', 'SMP'),
        ('sltp', 'SLTP'),
        ('sma', 'SMA'),
        ('smk', 'SMK'),
        ('smu', 'SMU'),
        ('slta', 'SLTA'),
        ('kuliah', 'Kuliah')
    ], string="Pendidikan")
