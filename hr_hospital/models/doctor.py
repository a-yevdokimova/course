import logging
from odoo import fields, models

_logger = logging.getLogger(__name__)


class Doctor(models.Model):
    _name = "doctor"
    _description = "Doctors Records"
    _inherit = "person"

    age = fields.Integer(racking=True)
    gender = fields.Selection([('male', 'Male'),
                               ('female', 'Female'),
                               ('others', 'Others')],
                              tracking=True)
    specialty = fields.Char()
    doctor_role = fields.Selection([
        ('intern', 'Intern'),
        ('mentor', 'Doctor Mentor')])
