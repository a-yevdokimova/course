import logging
from odoo import fields, models, api
from datetime import date
from dateutil.relativedelta import relativedelta

_logger = logging.getLogger(__name__)


class Patient(models.Model):
    _name = "patient"
    _description = "Patients Records"
    _inherit = "person"

    is_child = fields.Boolean("Is Child ?", tracking=True)
    gender = fields.Selection([('male', 'Male'),
                               ('female', 'Female'),
                               ('others', 'Others')],
                              tracking=True)
    doctor_id = fields.Many2one(string='Personal doctor', comodel_name='doctor',
                                domain="[('is_intern', '=', False)]")
    birthday = fields.Date(string='Date of Birth')
    age = fields.Integer(compute='_compute_age')
    passport = fields.Char()
    contact_person = fields.Char()

    @api.depends('birthday')
    def _compute_age(self):
        for rec in self:
            if rec.birthday:
                rec.age = relativedelta(
                    date.today(),
                    date(rec.birthday.year, rec.birthday.month, rec.birthday.day),
                ).years
            else:
                rec.age = False

    @api.onchange('age')
    def _onchange_age(self):
        if self.age <= 18:
            self.is_child = True
        else:
            self.is_child = False

    def action_view_patient_visits(self):
        return {
            'name': 'Patient Visits',
            'view_type': 'form',
            'view_mode': 'tree,form',
            'res_model': 'patient.visits',
            'domain': [('patient_id', '=', self.id)],
            'type': 'ir.actions.act_window',
            'context': {'search_default_patient_id': self.id}
        }

    def action_create_visits(self):
        self.ensure_one()
        return {
            'name': 'New Visits',
            'type': 'ir.actions.act_window',
            'res_model': 'patient.visits',
            'view_mode': 'form',
            'context': {'default_patient_id': self.id},
            'target': 'new'
        }
