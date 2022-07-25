from datetime import date

from odoo import api, fields, models


class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Hospital Patient"

    name = fields.Char(string="Name", tracking=True)
    birth_date = fields.Date(string="Birth Date")
    age = fields.Integer(string="Age", compute="calculate_age")
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string="gender", default='male')
    ref = fields.Char(string="Reference", default="Nitin")

    def calculate_age(self):
        for rec in self:
            if rec.birth_date:
                today = date.today()
                rec.age = today.year - rec.birth_date.year
            else:
                rec.age = False
