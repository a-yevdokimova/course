import logging
from odoo import fields, models, api

_logger = logging.getLogger(__name__)


class Diseases(models.Model):
    _name = "disease"
    _description = "Disease"

    name = fields.Char(required=True, tracking=True)
    description = fields.Text()
    # parent_id = fields.Many2one(comodel_name='disease')

    parent_id = fields.Many2one('disease', string='Parent Category', index=True, ondelete="cascade")
    parent_path = fields.Char(index=True, unaccent=False)
    child_id = fields.One2many('disease', 'parent_id', string='Children Categories')
    parents_and_self = fields.Many2many('disease', compute='_compute_parents_and_self')

    @api.constrains('parent_id')
    def check_parent_id(self):
        if not self._check_recursion():
            raise ValueError(_('Error! You cannot create recursive categories.'))

    @api.depends('parents_and_self')
    def _compute_display_name(self):
        for category in self:
            category.display_name = " / ".join(category.parents_and_self.mapped(
                lambda cat: cat.name or _("New")
            ))

    def _compute_parents_and_self(self):
        for category in self:
            if category.parent_path:
                category.parents_and_self = self.env['disease'].browse(
                    [int(p) for p in category.parent_path.split('/')[:-1]])
            else:
                category.parents_and_self = category