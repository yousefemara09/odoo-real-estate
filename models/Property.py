from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Property(models.Model):
    _name = 'property'
    _description = 'Real Estate Property'

    name = fields.Char(required=True)
    description = fields.Text()
    postcode = fields.Char(required=True)
    date_availability = fields.Date()
    expected_price = fields.Float(required=True)
    selling_price = fields.Float(readonly=True)

    bedrooms = fields.Integer(default=1)
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()

    garden_orientation = fields.Selection([
        ('north', 'North'),
        ('south', 'South'),
        ('east', 'East'),
        ('west', 'West')
    ], default='north')

    owner_id = fields.Many2one('owner')
    tag_ids = fields.Many2many('tag')

    _sql_constraints = [
        ('unique_name', 'unique(name)', 'Should be unique name'),
    ]

    @api.constrains('bedrooms')
    def _check_bedrooms(self):
        for record in self:
            if record.bedrooms < 1:
                raise ValidationError('Bedrooms must be greater than 0')

    @api.constrains('expected_price')
    def _check_expected_price(self):
        for record in self:
            if record.expected_price <= 0:
                raise ValidationError('Expected price must be greater than 0')
