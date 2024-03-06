import logging
from odoo import fields, models

_logger = logging.getLogger(__name__)


class DoctorSchedule(models.Model):
    _name = "doctor.schedule"
    _description = "Doctor`s Schedule"

    doctor_id = fields.Many2one(string='Personal doctor', comodel_name='doctor')
    appointment_date = fields.Date()
    appointment_time = fields.Float(string='Appointment Time', required=True)

    _sql_constraints = [
        (
            'appointment_unique', 'unique(appointment_date, appointment_time)',
            'Appointment time must be unique per date!')
    ]
