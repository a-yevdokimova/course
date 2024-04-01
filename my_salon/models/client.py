from odoo import api, fields, models
from odoo.exceptions import ValidationError
class Client(models.Model):
    _name = "client"
    _inherit = 'mail.thread'
    _description ="Client Records"

    name = fields.Char(string='Name', required=True, tracking=True)
    second_name = fields.Char(string='Second Name', required=True, tracking=True)
    image_1920 = fields.Image()
    age = fields.Integer(string='Age', tracking=True)
    is_child = fields.Boolean(string="Is Child ?", default=False, tracking=True)
    notes = fields.Text(string="Notes")
    gender = fields.Selection([('male','Male'), ('female', 'Female'), ('others', 'Others')], string="Gender", tracking=True)
    capitalized_name = fields.Char(string='Capitalized Name', compute='_compute_capitalized_name', store=True)
    ref = fields.Char(string="Reference", default=lambda self: ('New'))
    master_id = fields.Many2one('master', string="Masters")
    active = fields.Boolean(default=True)
    tag_ids = fields.Many2many('res.partner.category', 'client_tag_rel', 'clients_id', 'tag_id', string="Tags")


    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            vals['ref'] = self.env['ir.sequence'].next_by_code('client')
        return super(Client, self).create(vals_list)

    @api.constrains('is_child', 'age')
    def _check_child_age(self):
        for rec in self:
            if rec.is_child and rec.age == 0:
                raise ValidationError(("Age has to be recorder !"))

    @api.depends('name')
    def _compute_capitalized_name(self):
        for rec in self:
            if rec.name:
                rec.capitalized_name = rec.name.upper()
            else:
                rec.capitalized_name = ''


    @api.onchange('age')
    def _onchange_age(self):
        if self.age <= 18:
            self.is_child = True
        else:
            self.is_child = False