from datetime import date

from odoo import api, fields, models


class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Hospital Patient"

    name = fields.Char(string="Name", tracking=True)
    doctor_id = fields.Many2one('hospital.doctor',string="Doctor")
    birth_date = fields.Date(string="Birth Date")
    age = fields.Integer(string="Age", compute="calculate_age")
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string="gender")
    ref = fields.Char(string="Reference")

    def calculate_age(self):
        for rec in self:
            if rec.birth_date:
                today = date.today()
                rec.age = today.year - rec.birth_date.year
            else:
                rec.age = False

    @api.model
    def create(self, x):
        # values['name'] = 'Nitin'
        res = super(HospitalPatient, self).create(x)
        print('.........................................', res)
        print('.........................................', x)
        print('.........................................', self.doctor_id.doctor)
        return res

    def copy(self, default={}):
        default['name'] = "copy " + self.name + ""
        res = super(HospitalPatient, self).copy(default=default)
        res.gender = 'female'
        return res

    @api.model
    def search(self, args, offset=0, limit=None, order=None, count=False):
        res = super(HospitalPatient, self).search(args, limit=5, order='name asc')
        return res

    # def name_get(self):
    #     lis = []
    #     for rec in self:
    #         name = str(rec.id) + str(rec.name)
    #         lis.append((rec.id, name))
    #     return lis

    @api.model
    def _name_search(self, name='', args=None, operator='ilike', limit=100, name_get_uid=None):
        args = list(args or [])
        print('...................................................',args)
        # optimize out the default criterion of ``ilike ''`` that matches everything
        if not (name == '' and operator == '='):
            args += ['|', (self._rec_name, operator, name), ('gender', operator, name)]
        print('...................................................',args)
        return self._search(args, limit=limit, access_rights_uid=name_get_uid)


