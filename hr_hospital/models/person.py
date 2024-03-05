import logging
from odoo import fields, models

_logger = logging.getLogger(__name__)


class Person(models.AbstractModel):
    _name = "person"
    _description = "Person"

    phone = fields.Char()
    email = fields.Char()
    image = fields.Image()
