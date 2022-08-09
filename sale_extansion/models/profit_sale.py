from odoo import api, fields, models


class SaleOrderInherit(models.Model):
    _inherit = ['sale.order.line']

    profit = fields.Float(string="Profit")
    product_type_custom = fields.Selection(string="Product Type", related='product_id.detailed_type')

    tax_ids = fields.Float(string="Taxes")

    @api.onchange('product_id', 'tax_ids')
    def onchange_profit(self):
        for rec in self:
            if rec.product_id.standard_price:
                rec.profit = rec.product_id.lst_price - rec.product_id.standard_price

            if rec.tax_ids:
                rec.price_subtotal = (rec.product_id.lst_price * rec.tax_ids) / 100 + rec.product_id.lst_price

    def _prepare_invoice_line(self, **optional_values):
        res = super(SaleOrderInherit, self)._prepare_invoice_line()
        print('..................................xxxxxxxxxxxxx.....................',(self.product_type_custom))
        res['product_type_custom_invoice'] = self.product_id.detailed_type
        return res


class AccountMoveInherit(models.Model):
    _inherit = ['account.move.line']

    product_type_custom_invoice = fields.Char(string="Product Type")

