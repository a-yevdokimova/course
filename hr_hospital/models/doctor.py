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
    specialty = fields.Selection([('cardiology', 'Cardiology'),
                                  ('neurology', 'Neurology'),
                                  ('ophthalmology', 'Ophthalmology')],
                                 tracking=True)
    is_intern = fields.Boolean(string='Intern')
    mentor_id = fields.Many2one('doctor', string='Doctor Mentor', domain="[('is_intern', '!=', True)]")

