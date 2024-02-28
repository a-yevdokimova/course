import logging
from odoo import fields, models

_logger = logging.getLogger(__name__)


class Patient(models.Model):
    _name = "patient"
    _description = "Patients Records"

    name = fields.Char(string='Name', required=True, tracking=True)
    second_name = fields.Char(string='Second Name', required=True,
                              tracking=True)
    age = fields.Integer(string='Age', tracking=True)
    is_child = fields.Boolean(string="Is Child ?", tracking=True)
    gender = fields.Selection([('male', 'Male'),
                               ('female', 'Female'),
                               ('others', 'Others')],
                              string="Gender", tracking=True)
