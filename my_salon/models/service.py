from odoo import api, fields, models
from odoo.exceptions import ValidationError

class Service(models.Model):
    _name = "service"
    _description ="Clients Records"

    name = fields.Char(string='Name', required=True, tracking=True)