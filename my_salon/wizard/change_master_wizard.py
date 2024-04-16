from odoo import models, fields


class ChangeMasterWizard(models.TransientModel):
    _name = 'change.master.wizard'
    _description = 'Change master wizard'

    client_id = fields.Many2one('client')
    master_id = fields.Many2one('master', string='New Master')

    def action_change(self):
        self.ensure_one()
        self.client_id.master_id = self.master_id.id
