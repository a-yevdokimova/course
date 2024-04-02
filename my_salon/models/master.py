from odoo import api, fields, models

class Master(models.Model):
    _name = "master"
    _inherit = 'mail.thread'
    _description = "Master Records"

    name = fields.Char(string='Name', required=True, tracking=True)
    second_name = fields.Char(string='Second Name', required=True, tracking=True)
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('others', 'Others')], string="Gender",
                              tracking=True)
    ref = fields.Char(string="Reference", default=lambda self: ('New'))
    active = fields.Boolean(default=True)
    service_ids = fields.Many2many(comodel_name='my_service')
    image_1920 = fields.Image()
    avatar_128 = fields.Image(related='image_1920', max_width=128, max_height=128)

    def name_get(self):
        res = []
        for rec in self:
            res.append((rec.id, f'{rec.ref} - {rec.name}'))
        return res