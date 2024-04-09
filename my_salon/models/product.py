from odoo import fields, models

class Product(models.Model):
    """
        Represents a product in the system.

        This model tracks essential information about products, such as their name,
        description, price, and associated providers. It's a fundamental part of managing
        inventory and supplier relationships within the system.
    """

    _name = "product"

    name = fields.Char(string='Name', required=True, tracking=True)
    description = fields.Text()
    price = fields.Float()
    provider_ids = fields.Many2many(comodel_name='provider')
    currency_id = fields.Many2one('res.currency', string="Currency")
