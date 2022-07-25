from odoo import api, fields, models


class Course(models.Model):
    _name = "school.course"
    _description = "Course Detail"
    _rec_name = "course_name"

    course_name = fields.Selection([
        ('science', 'Science'),
        ('commerce', 'Commerce'),
        ('arts', 'Arts'),
    ], string="Select Course")
    # course_name_2 = fields.Many2many('school.subject', 'subject_course_ref')
    course_fee = fields.Integer(string="Course Fee")
    bus_fee = fields.Integer(string="Bus Fee")
    total_fee = fields.Integer(string="Total Fee", compute='calculate_total_fee')

    @api.depends('course_fee', 'bus_fee')
    def calculate_total_fee(self):
        for rec in self:
            rec.total_fee = rec.bus_fee + rec.course_fee

    student_course_ids = fields.One2many("school.student", "s_course_id", string="Course Details")
