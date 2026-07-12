from odoo import models , fields


class ChangeWizardState(models.TransientModel):
    _name = 'change.state'
    _description = 'Change State'

    property_id = fields.Many2one('property')

    state = fields.Selection([
        ('draft' , 'Draft'),
        ('rejected' , 'Rejected'),
    ], default='draft')

    reason = fields.Char()

    def action_confirm(self):
        if self.property_id.state == 'closed':
            self.property_id.state = self.state
            self.property_id.create_history('closed', self.property_id.state)

