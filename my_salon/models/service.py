from odoo import fields, models


class Service(models.Model):
    """
        Represents a service provided by the company.

        This model stores information about various services offered, including their name,
        price, associated products, service providers (masters), and the duration of the service.
        The active field indicates whether the service is currently offered.
    """
    _name = "my_service"
    _description = "Service Records"

    name = fields.Char(string='Name', required=True, tracking=True)
    price = fields.Float()
    product_ids = fields.Many2many(comodel_name='product')
    master_ids = fields.Many2many(comodel_name='master')
    duration = fields.Float(string='Duration (hours)', required=True)
    active = fields.Boolean(default=True)


