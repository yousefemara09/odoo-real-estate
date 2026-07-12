from odoo import models, fields, api
from odoo.exceptions import ValidationError
import requests , json

class Property(models.Model):
    _name = 'property'
    _description = 'Property'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(required=True)
    # name = fields.Char(required=True , translate=True)

    ref = fields.Char(readonly=True ,default='New')
    description = fields.Text()
    postcode = fields.Char(required=True)
    date_availability = fields.Date(tracking=True)
    check_selling_date = fields.Date(tracking=True)
    is_date = fields.Boolean()
    expected_price = fields.Float()
    selling_price = fields.Float()
    diff = fields.Float(compute='_compute_diff' , store=True)
    bedrooms = fields.Integer(default=1)
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    active = fields.Boolean(default=True)
    garden_orientation = fields.Selection([
        ('north', 'North'),
        ('south', 'South'),
        ('east', 'East'),
        ('west', 'West')
    ], default='north')

    owner_id = fields.Many2one('owner')
    tag_ids = fields.Many2many('tag')

    owner_address = fields.Char(related='owner_id.address')
    owner_phone = fields.Char(related='owner_id.phone')


    line_ids = fields.One2many('property.line', 'property_id', string='Property')

    state = fields.Selection([
        ('draft', 'Draft'),
        ('sold', 'Sold'),
        ('rejected', 'Rejected'),
        ('closed' , 'Closed'),
    ], default='draft')

    _sql_constraints = [
        ('unique_name', 'unique(name)', 'Should be unique name'),
    ]

    @api.depends('expected_price', 'selling_price')
    def _compute_diff(self):
        for record in self:
            record.diff = record.expected_price - record.selling_price

    # @api.onchange('expected_price')
    # def _check_expected_price(self):
    #     if self.expected_price <= 0:
    #         return {
    #             'warning': {
    #                 'title': 'Warning',
    #                 'message': 'Expected price must be greater than 0',
    #                 'type': 'notification',
    #             }
    #         }

    @api.constrains('expected_price')
    def _check_expected_price(self):
        for record in self:
            if record.expected_price <= 0:
                raise ValidationError('Expected price must be greater than 0')



    @api.constrains('bedrooms')
    def _check_bedrooms(self):
        for record in self:
            if record.bedrooms < 1:
                raise ValidationError('Bedrooms must be greater than 0')


    def _check_expected_selling_date(self):
        property_ids = self.search([])
        for record in property_ids:
            if record.check_selling_date and record.check_selling_date < fields.Date.today():
                record.is_date = True

    def action_sold(self):
        for record in self:
            record.create_history(record.state , 'sold')
            record.state = 'sold'

    def action_rejected(self):
        for record in self:
            record.create_history(record.state , 'rejected')
            record.state = 'rejected'

    def action_draft(self):
        for record in self:
            record.create_history(record.state , 'draft')
            record.state = 'draft'

    def action_closed(self):
        for record in self:
            record.create_history(record.state , 'closed')
            record.state = 'closed'


    def create_history(self , old_state , new_state , reason=""):
        for record in self:
            record.env['property.history'].create({
                'user_id': record.env.uid,
                'property_id': record.id,
                'old_state': old_state,
                'new_state': new_state,
                'reason': reason or '',
                'line_ids' : [(0, 0, {'description': line.description , 'area': line.area}) for line in record.line_ids],
                'tag_history_ids' : [ (0, 0, {'tag_id': tag.id }) for tag in record.tag_ids ],
            })

    def action_change_wizard_state(self):
        action = self.env['ir.actions.actions']._for_xml_id('app_one.change_wizard_state_action')
        action['context'] = {'default_property_id': self.id  }
        return  action




    def action(self):
        res = self.env['property'].search([
            '&',
            ('name' , 'like' , 'Property1') ,
            ('postcode' , '=' , 123456)
        ])
        print(res)



    @api.model
    def create(self, vals):
        record = super(Property, self).create(vals)
        if record.ref == 'New':
            record.ref = self.env['ir.sequence'].next_by_code('property.seq')
        return record

    def action_open_related_owner(self):

        action = self.env['ir.actions.act_window']._for_xml_id('app_one.owner_action')
        view_form = self.env.ref('app_one.owner_view_form')

        action['res_id'] = self.owner_id.id
        action['views'] = [(view_form.id, 'form')]

        return action

    def action_open_related_tag(self):
        act = self.env['ir.actions.act_window']._for_xml_id('app_one.tag_action')
        view = self.env.ref('app_one.tag_view_form')
        act['res_id'] =self.tag_ids[:1].id
        act['views'] = [(view.id, 'form')]

        return act
    def get_properties(self):
        payload = dict()#تضيف data=payload في الـ POST / PUT بس — لما بتبعت data في الـ body:
        response = requests.get('http://emara:8070/v1/properties', data= payload)
        if response.status_code == 200:
            print(response.content)
        else:
            raise ValidationError('Property not found')

    # def get_properties(self):
    #     response = requests.get('http://emara:8070/v1/properties')
    #     response_json = response.json()
    #     print(response_json)

    def report_execl_print(self):
        return {
            'type': 'ir.actions.act_url',
            'url': f'/property/excel/report/{self.ids}',
            'target': 'new',
        }

class PropertyLine(models.Model):
    _name = 'property.line'
    _description = 'Property Line'

    property_id = fields.Many2one('property')

    area=fields.Float()
    description = fields.Char(required=True)

