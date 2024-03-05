import logging
from odoo import fields, models

_logger = logging.getLogger(__name__)


class Diseases(models.Model):
    _name = "disease"
    _description = "Disease"

    name = fields.Char(required=True, tracking=True)
    description = fields.Text()
