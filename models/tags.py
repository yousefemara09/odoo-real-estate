from odoo import api, fields, models

class Tags(models.Model):
    _name = 'tag'
    name = fields.Char(required=True)
    property_ids = fields.Many2many('property')

    history_ids = fields.One2many('property.history.tag', 'tag_id' )
