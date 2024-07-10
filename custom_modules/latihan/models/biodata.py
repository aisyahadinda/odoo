from odoo import models, fields, api
from datetime import date

class Biodata(models.Model):
    _name = "latihan.biodata"

    name = fields.Char(string="Nama")
    fullname = fields.Char(string="Nama Lengkap")
    birth_date = fields.Date(string="Tanggal Lahir")
    age = fields.Integer(string="Umur", compute='_compute_age', store=True)
    children = fields.Integer(string="Anak")
    photo = fields.Image(string="Foto")
    gender = fields.Selection(
        [('perempuan', 'Perempuan'), ('laki_laki', 'Laki-laki')],
        string="Jenis Kelamin"
    )    
    religion = fields.Selection(
        [
            ('islam', 'Islam'),
            ('kristen', 'Kristen'),
            ('katolik', 'Katolik'),
            ('hindu', 'Hindu'),
            ('budha', 'Budha'),
            ('konghucu', 'Konghucu')
        ],
        string="Agama"
    ) 
    education_sd = fields.Boolean(string="SD")
    education_smp = fields.Boolean(string="SMP")
    education_sltp = fields.Boolean(string="SLTP")
    education_sma = fields.Boolean(string="SMA")
    education_smk = fields.Boolean(string="SMK")
    education_smu = fields.Boolean(string="SMU")
    education_slta = fields.Boolean(string="SLTA")
    education_kuliah = fields.Boolean(string="Kuliah")
    
    @api.depends('birth_date')
    def _compute_age(self):
        for rec in self:
            if rec.birth_date:
                today = date.today()
                birth_date = fields.Date.from_string(rec.birth_date)
                age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
                rec.age = age
            else:
                rec.age = 0

    def calculate_age(self):
        self._compute_age()
