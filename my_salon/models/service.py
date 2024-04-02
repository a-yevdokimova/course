from odoo import api, fields, models
from odoo.exceptions import ValidationError

class Service(models.Model):
    _name = "my_service"
    _description ="Service Records"

    name = fields.Char(string='Name', required=True, tracking=True)
    price = fields.Float()
    product_ids = fields.Many2many(comodel_name='product')
    master_ids = fields.Many2many(comodel_name='master')
    duration = fields.Float(string='Duration (hours)', required=True)
    active = fields.Boolean(default=True)
