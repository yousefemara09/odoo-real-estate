from odoo import fields, models, api

class ResPartner(models.Model):
    _inherit = 'res.partner'

    price = fields.Float(compute='_compute_price', store=True)

    property_id = fields.Many2one('property')


    @api.depends('property_id')
    def _compute_price(self):
        for res in self:
            res.price = res.property_id.selling_price