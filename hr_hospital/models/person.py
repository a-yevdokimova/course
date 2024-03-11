import logging
from odoo import fields, models

_logger = logging.getLogger(__name__)


class Person(models.AbstractModel):
    _name = "person"
    _description = "Person"

    name = fields.Char(required=True)
    second_name = fields.Char(required=True)
    phone = fields.Char()
    email = fields.Char()
    image = fields.Image()
