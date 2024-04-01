from odoo import api, fields, models

class Master(models.Model):
    _name = "master"
    _inherit = 'mail.thread'
    _description = "Master Records"
    _rec_name = 'ref'

    name = fields.Char(string='Name', required=True, tracking=True)
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('others', 'Others')], string="Gender",
                              tracking=True)
    ref = fields.Char(string="Reference", required=True)
    active = fields.Boolean(default=True)

    def name_get(self):
        res = []
        for rec in self:
            res.append((rec.id, f'{rec.ref} - {rec.name}'))
        return res