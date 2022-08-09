from odoo import api, fields, models


class HospitalPatient2(models.Model):
    _name = "hospital.appointment"
    _description = "Hospital Appointment"
    _rec_name = "patient_id"

    patient_id = fields.Many2one("hospital.patient", string="Patient")
    patient_ids = fields.Many2many("hospital.patient", string="Patients")
    gender = fields.Selection(related="patient_id.gender")
    age = fields.Integer(string="Age", related="patient_id.age")
    appointment_time = fields.Datetime(string="Appointment Time", default=fields.Datetime.now)
    booking_date = fields.Date(string="Booking Date")
    ref = fields.Char(string="Reference", default="AAAAA")
    prescription = fields.Html(string="Prescription")



    @api.model
    def default_get(self, field_list=[]):
        print(field_list)
        rtn = super(HospitalPatient2, self).default_get(field_list)
        print('..................................'
              '...............................'
              '..........................'
              '........', rtn)
        return rtn

    #
    # def active_search(self):
    #     for rec in self:
    #         search and search_count
    #         patients = self.env['hospital.patient'].search_read([])
    #         print('.......................................'
    #               '..................................................'
    #               '.........................................'
    #               '...........................................'
    #               '.............................................'
    #               '................................. read', patients)
    #         patients_count = self.env['hospital.patient'].search_count([])
    #         print(patients_count)
    #         # browse and exists
    #         patients_browse = self.env['hospital.patient'].browse(100)
    #         if patients_browse.exists():
    #             print(patients_browse)
    #         else:
    #             print("Not available")
    #         create
    #         values = {
    #             'name': 'Hardik'
    #         }
    #         patients_create = self.env['hospital.patient'].create(values)
    #         write
    #         values1 = {
    #             'name': 'Mihir',
    #             'gender': 'male'
    #         }
    #         patients_browse1 = self.env['hospital.patient'].browse(1)
    #         if patients_browse1.exists():
    #             patients_write = patients_browse1.write(values1)
    #
    #         copy
    #         patients_copy = self.env['hospital.patient'].browse(1)
    #         """1 var delete thai jai atle id change karvi pade"""
    #         patients_copy.copy()
    #         patients_copy.unlink()

    @api.onchange('patient_id')
    def onchange_ref(self):
        for rec in self:
            if rec.patient_id:
                rec.ref = rec.patient_id.ref


