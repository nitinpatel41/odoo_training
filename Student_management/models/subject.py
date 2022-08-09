from odoo import api, fields, models


class Subject(models.Model):
    _name = "school.subject"
    _description = "Subject Details"


    name = fields.Many2one("school.student", string="Student Name")
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string='Gender', related='name.gender')
    total = fields.Integer(string="Total Subject")
    sub1 = fields.Char(string="Subject1 Name")
    sub2 = fields.Char(string="Subject2 Name")
    sub3 = fields.Char(string="Subject3 Name")
    sub4 = fields.Char(string="Subject4 Name")
    sub5 = fields.Char(string="Subject5 Name")
    priority = fields.Selection([
        ('0', 'Normal'),
        ('1', 'Low'),
        ('2', 'High'),
        ('3', 'Very High')], string="Priority"
    )


