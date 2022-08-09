from odoo import api, fields, models


class HospitalDoctor(models.Model):
    _name = "hospital.doctor"


    name = fields.Char(string="name")
    doctor = fields.Many2one("res.users", string="Patient")
