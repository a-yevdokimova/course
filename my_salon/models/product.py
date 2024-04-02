from odoo import api, fields, models
from odoo.exceptions import ValidationError
class Product(models.Model):
    _name = "product"

    name = fields.Char(string='Name', required=True, tracking=True)