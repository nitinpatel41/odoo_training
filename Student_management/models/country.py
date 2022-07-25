from odoo import api, fields, models


class Country(models.Model):
    _name = "student.country"
    _description = "Student Country"

    student_name_ids = fields.One2many("school.student", "current_country_id", string="No of Student")
    name = fields.Char(string="Name")
    country_code = fields.Char(string="Country Code")
