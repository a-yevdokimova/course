import logging
from odoo import fields, models

_logger = logging.getLogger(__name__)


class Diagnosis(models.Model):
    _name = "diagnosis"
    _description = "Patients Diagnosis"

    visit_id = fields.Many2one(comodel_name='patient.visits')
    doctor_id = fields.Many2one(comodel_name='doctor')
    patient_id = fields.Many2one(comodel_name='patient')
    disease_id = fields.Many2one(comodel_name='disease')
    appointment = fields.Text(string='Appointment for treatment', help='Призначення для лікування')

