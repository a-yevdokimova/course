from odoo import api, fields, models
from odoo.exceptions import ValidationError
class Product(models.Model):
    _name = "product"

    name = fields.Char(string='Name', required=True, tracking=True)
    description = fields.Text()
    price = fields.Float()
    provider_ids = fields.Many2many(comodel_name='provider')