from odoo import api, fields, models
from odoo.exceptions import ValidationError
class Provider(models.Model):
    """
        Represents a provider or supplier in the system.

        This model is essential for tracking the providers or suppliers of products,
        including their contact information and the products they supply. It allows
        for managing relationships with these entities and understanding product
        sourcing within the system.
    """

    _name = "provider"

    name = fields.Char(string='Name', required=True, tracking=True)
    phone = fields.Char()
    address = fields.Text()
    product_ids = fields.Many2many(comodel_name='product')