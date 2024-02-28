import logging
from odoo import fields, models

_logger = logging.getLogger(__name__)


class PatipatientsVisits(models.Model):
    _name = "patient.visits"
    _description = "Patients Visits"

    number = fields.Integer()
    description = fields.Text()
