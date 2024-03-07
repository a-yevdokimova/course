from odoo import models, fields, _


class ChangeDoctorWizard(models.TransientModel):
    _name = 'change.doctor.wizard'
    _description = 'Change Doctor Wizard'

    doctor_id = fields.Many2one('doctor', string='New Doctor', required=True)

    def action_open_wizard(self):
        return {
            'name': _('Change Doctor Wizard'),
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'res_model': 'change.doctor.wizard',
            'target': 'new',
            # 'context': {'default_country_id': self.env.user.country_id.id},
        }


    # def change_doctor(self):
    #     active_ids = self.env.context.get('active_ids')
    #     patients = self.env['patient'].browse(active_ids)
    #     for patient in patients:
    #         patient.write({'doctor_id': self.doctor_id.id})
    #     return {'type': 'ir.actions.act_window_close'}