from odoo import api, fields, models
from odoo.exceptions import ValidationError
class Provider(models.Model):
    _name = "provider"

    name = fields.Char(string='Name', required=True, tracking=True)
    phone = fields.Char()
    address = fields.Text()
    product_ids = fields.Many2many(comodel_name='product')