import logging
from odoo import fields, models

_logger = logging.getLogger(__name__)


class HistoryChange(models.Model):
    _name = "history.change"
    _description = "History of changes of the personal doctor"

    appointment_date = fields.Datetime()
    doctor_id = fields.Many2one(comodel_name='doctor')
    patient_id = fields.Many2one(comodel_name='patient')