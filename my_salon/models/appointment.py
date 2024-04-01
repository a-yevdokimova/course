from odoo import api, fields, models
from odoo.exceptions import ValidationError

class Appointment(models.Model):
    _name = "appointment"
    _description ="Clients Records"

    name = fields.Char(string='Name', required=True, tracking=True)