import logging
from odoo import fields, models

_logger = logging.getLogger(__name__)


class Doctor(models.Model):
    _name = "doctor"
    _description = "Doctors Records"

    name = fields.Char(string='Name', required=True, tracking=True)
    second_name = fields.Char(string='Second Name', required=True,
                              tracking=True)
    age = fields.Integer(string='Age', tracking=True)
    gender = fields.Selection([('male', 'Male'),
                               ('female', 'Female'),
                               ('others', 'Others')],
                              string="Gender", tracking=True)
