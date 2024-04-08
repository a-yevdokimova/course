from odoo import api, fields, models
from odoo.exceptions import ValidationError
class ResCompany(models.Model):
    """
        Extends the default Odoo Company model (`res.company`) to include social media contact information.

        This extension adds fields for Instagram and Telegram, allowing companies to store
        their social media handles directly within their company profile. This enhancement
        makes it easier to include social media information in communications, reports, and
        other company-related outputs.
    """

    _inherit = 'res.company'

    instagram = fields.Char()
    telegram = fields.Char()