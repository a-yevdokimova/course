import logging
from odoo import fields, models

_logger = logging.getLogger(__name__)


class Diseases(models.Model):
    _name = "diseases"
    _description = "Diseases"

    name = fields.Char(string='Name', required=True, tracking=True)
    description = fields.Text(string='Description')
