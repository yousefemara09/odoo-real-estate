from odoo import api, fields, models

class Tags(models.Model):
    _name = 'tag'
    name = fields.Char(required=True)
    property_ids = fields.Many2one('property')
