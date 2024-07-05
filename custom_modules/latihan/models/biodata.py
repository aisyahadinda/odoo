from odoo import models, fields

class Biodata(models.Model):
    _name = "latihan.biodata"

    name = fields.Char(string="Nama")
    fullname = fields.Char(string="Nama Lengkap")
    birth_date = fields.Date(string="Tanggal Lahir")
    age = fields.Integer(string="Umur")
    children = fields.Integer(string="Anak ke-")
    photo = fields.Image(string="Foto")
    gender = fields.Char(string="Jenis Kelamin")
    education_sd = fields.Boolean(string="SD")
    education_smp = fields.Boolean(string="SMP")
    education_sltp = fields.Boolean(string="SLTP")
    education_sma = fields.Boolean(string="SMA")
    education_smk = fields.Boolean(string="SMK")
    education_smu = fields.Boolean(string="SMU")
    education_slta = fields.Boolean(string="SLTA")
    education_kuliah = fields.Boolean(string="Kuliah")
