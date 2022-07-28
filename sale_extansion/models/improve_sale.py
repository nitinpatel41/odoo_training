from odoo import api, fields, models


class SaleOrderInherit(models.Model):
    _inherit = ['sale.order']

    if 'partner_id.phone':
        contact = fields.Char(string="Contact No", related=('partner_id.phone' or 'partner_id.mobile'))

    ave = fields.Char(string="Average", compute="cal_ave")

    def cal_ave(self):
        for rec in self:
            print(len(rec.order_line))
            print('.............................................................................', rec.tax_totals_json)
            rec.ave = rec.amount_total / len(rec.order_line)
