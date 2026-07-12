from odoo import api, fields, models

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    property_id = fields.Many2one('property')

    def action_confirm(self):
        rec = super(SaleOrder,self).action_confirm()
        print("Confirm IS Done")
        return rec

    def action_do_something(self):
        print(self, "inside do something")

