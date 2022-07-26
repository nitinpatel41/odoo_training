from odoo import api, fields, models


class SaleOrderInherit(models.Model):
    _inherit = ['sale.order']

    contact = fields.Char(string="Contact No")
