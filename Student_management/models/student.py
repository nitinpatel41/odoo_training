from datetime import date

from odoo import api, fields, models, _
from odoo.exceptions import ValidationError, UserError


class Student(models.Model):
    _name = "school.student"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Student Detail"
    # _rec_name = "student_name"

    surname = fields.Char(string="Student Surname")
    student_name = fields.Char(string="Student Name")
    father_name = fields.Char(string="Father Name", tracking=True)
    religion = fields.Html(string="Religion", required=True, copy=False, )

    std = fields.Integer(string="Stander")
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string='Gender')
    image = fields.Binary(string="Student Image")
    birth_date = fields.Date(string="Birth Date")
    age = fields.Integer(string="Age", compute="calculate_age")

    @api.depends('birth_date')
    def calculate_age(self):
        for rec in self:
            if rec.birth_date:
                today = date.today()
                print("agggeeeeeeeeeeeeeeeeeeee", today.year - rec.birth_date.year)
                rec.age = today.year - rec.birth_date.year
            else:
                rec.age = False

    # _sql_constraint = [
    #     'age_check', 'CHECK(age!=0)', 'Age is 0. it is not allowed'
    # ]

    @api.constrains('birth_date')
    def check_age(self):
        for rec in self:
            if rec.age and rec.age >= 29:
                raise ValidationError(_("Your Age  is greater than 29"))

    current_house_no = fields.Char(string="House No")
    current_street = fields.Char(string="Street")
    current_area = fields.Char(string="Area Name")
    current_city = fields.Char(string="City")
    current_taluka = fields.Char(string="Taluka")
    current_dis = fields.Char(string="District")
    current_pincode = fields.Integer(string="Pincode")
    current_state = fields.Char(string="State")
    current_country_id = fields.Many2one("student.country", string="Country")

    as_per_current_address = fields.Boolean(string="As per Current Address")

    house_no = fields.Char(string="House No")
    street = fields.Char(string="Street")
    area = fields.Char(string="Area Name")
    city = fields.Char(string="City")
    taluka = fields.Char(string="Taluka")
    dis = fields.Char(string="District")
    pincode = fields.Integer(string="Pincode")
    state = fields.Char(string="State")
    country = fields.Char(string="Country")

    @api.onchange('as_per_current_address')
    def onchange_as_per_current_address(self):
        for rec in self:
            if rec.as_per_current_address:
                rec.house_no = rec.current_house_no
                rec.street = rec.current_street
                rec.area = rec.current_area
                rec.city = rec.current_city
                rec.taluka = rec.current_taluka
                rec.dis = rec.current_dis
                rec.pincode = rec.current_pincode
                rec.state = rec.current_state
                rec.country = rec.current_country_id

    s_course_id = fields.Many2one("school.course", string="Enter Stream")

    state1 = fields.Selection([('abc', 'Abc'),
                               ('pqr', 'Pqr'),
                               ('xyz', 'Xyz')])

    def name_get(self):
        student_list = []
        for rec in self:
            name = str(rec.surname) + str(rec.student_name)
            student_list.append((rec.id, name))
        return student_list
