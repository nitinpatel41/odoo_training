from odoo import api, fields, models


class SaleOrderInherit(models.Model):
    _inherit = ['sale.order.line']
    _inherits = {'product.product' : 'lst_price'}

    profit = fields.Char(string="Profit")


    @api.onchange('')


