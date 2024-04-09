from odoo import api, fields, models
from odoo.exceptions import ValidationError


class Client(models.Model):
    """
        A model representing a client in the beauty salon system.

        It keeps track of client information, including personal details,
        gender, age, and related records like appointments. This model
        also leverages Odoo's mail thread for communications and tracking changes
    """

    _name = "client"
    _inherit = 'mail.thread'
    _description = "Client Records"

    name = fields.Char(string='Name', required=True, tracking=True)
    second_name = fields.Char(string='Second Name', required=True,
                              tracking=True)
    image_1920 = fields.Image()
    age = fields.Integer(string='Age', tracking=True)
    is_child = fields.Boolean(string="Is Child ?", default=False,
                              tracking=True)
    notes = fields.Text(string="Notes")
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('others', 'Others')],
                              string="Gender",
                              tracking=True)
    capitalized_name = fields.Char(string='Capitalized Name', compute='_compute_capitalized_name',
                                   store=True)
    ref = fields.Char(string="Reference", default=lambda self: ('New'))
    master_id = fields.Many2one('master', string="Masters")
    active = fields.Boolean(default=True)
    avatar_128 = fields.Image(related='image_1920', max_width=128,
                              max_height=128)
    tag_ids = fields.Many2many('res.partner.category',
                               'client_tag_rel',
                               'clients_id',
                               'tag_id', string="Tags")

    @api.model_create_multi
    def create(self, vals_list):
        """
        Overrides the default create method to set a unique reference for new clients.
        """
        for vals in vals_list:
            vals['ref'] = self.env['ir.sequence'].next_by_code('client')
        return super(Client, self).create(vals_list)

    @api.constrains('is_child', 'age')
    def _check_child_age(self):
        """
        Validates that clients marked as children have a non-zero age.
        Raises:
        ValidationError: If a child client has an age of 0.
        """
        for rec in self:
            if rec.is_child and rec.age == 0:
                raise ValidationError(("Age has to be recorder !"))

    @api.depends('name')
    def _compute_capitalized_name(self):
        """
        Computes the capitalized name of the client based on their name field.
        """
        for rec in self:
            if rec.name:
                rec.capitalized_name = rec.name.upper()
            else:
                rec.capitalized_name = ''

    @api.onchange('age')
    def _onchange_age(self):
        """
        Automatically marks clients as children if they are 18 years old or younger.
        """
        if self.age <= 18:
            self.is_child = True
        else:
            self.is_child = False

    def action_view_client_visits(self):
        """
        Returns an action to view the list of visits for the client.
        """
        return {
            'name': 'Client Visits',
            'view_type': 'form',
            'view_mode': 'tree,form',
            'res_model': 'appointment',
            'domain': [('client_id', '=', self.id)],
            'type': 'ir.actions.act_window',
            'context': {'search_default_client_id': self.id}
        }

    def action_create_visits(self):
        """
        Returns an action to create a new visit for the client.
        """
        self.ensure_one()
        return {
            'name': 'New Visits',
            'type': 'ir.actions.act_window',
            'res_model': 'appointment',
            'view_mode': 'form',
            'context': {'default_client_id': self.id},
            'target': 'new'
        }

