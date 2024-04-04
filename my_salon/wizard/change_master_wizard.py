from odoo import models, fields, _


class ChangeMasterWizard(models.TransientModel):
    _name = 'change.master.wizard'
    _description = 'Change master wizard'

    client_id = fields.Many2one('client')
    master_id = fields.Many2one('master', string='New Master')

    # def action_open_wizard(self):
    #     return {
    #         'name': _('Change master wizard'),
    #         'type': 'ir.actions.act_window',
    #         'view_mode': 'form',
    #         'res_model': 'change.master.wizard',
    #         'target': 'new',
    #     }

    def action_change(self):
        return
