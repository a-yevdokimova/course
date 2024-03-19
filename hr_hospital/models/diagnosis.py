import logging
from odoo import fields, models

_logger = logging.getLogger(__name__)


class Diagnosis(models.Model):
    _name = "diagnosis"
    _description = "Patients Diagnosis"

    visit_id = fields.Many2one(comodel_name='patient.visits')
    disease_id = fields.Many2one(comodel_name='disease')
    approved = fields.Boolean()
    appointment = fields.Text(string='Appointment for treatment', help='Призначення для лікування')

    visit_date = fields.Datetime(related='visit_id.visit_date', store=True)

    # doctor_id = fields.Many2one(comodel_name='doctor')
    # patient_id = fields.Many2one(comodel_name='patient')

