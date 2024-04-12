from odoo import fields, models


class Master(models.Model):
    """
       Represents a salon master (employee) within the system.

       This model tracks the master's personal details, including their name, gender, and services they provide.
       It inherits from 'mail.thread' to enable messaging and tracking. Each master can be associated with
       multiple services and appointments, allowing for detailed record-keeping and scheduling.
    """
    _name = "master"
    _inherit = 'mail.thread'
    _description = "Master Records"

    name = fields.Char(required=True, tracking=True)
    second_name = fields.Char(required=True,
                              tracking=True)
    gender = fields.Selection([('male', 'Male'),
                               ('female', 'Female'),
                               ('others', 'Others')],
                              tracking=True)
    ref = fields.Char(string="Reference", default=lambda self: ('New'))
    active = fields.Boolean(default=True)
    service_ids = fields.Many2many(comodel_name='my_service')
    image_1920 = fields.Image()
    avatar_128 = fields.Image(related='image_1920', max_width=128,
                              max_height=128)
    appointment_id = fields.One2many('appointment', 'master_id')

    def name_get(self):
        """
        Customizes the display name of the master records.
        Combines the master's reference and name for a more descriptive display in the UI.
        Returns:
        list: A list of tuples (id, display_name) for each master.
        """
        res = []
        for rec in self:
            res.append((rec.id, f'{rec.ref} - {rec.name}'))
        return res
