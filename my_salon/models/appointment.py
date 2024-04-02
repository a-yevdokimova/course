from odoo import api, fields, models
from odoo.exceptions import ValidationError

class Appointment(models.Model):
    _name = "appointment"
    _description ="Appointment Records"

    client_id = fields.Many2one('client', required=True)
    master_id = fields.Many2one('master', required=True)
    service_id = fields.Many2one('my_service', required=True)
    start_time = fields.Datetime()
    end_time = fields.Datetime()

    @api.constrains('start_time', 'end_time')
    def _check_time_range(self):
        for record in self:
            if record.start_time >= record.end_time:
                raise ValidationError("Start time must be earlier than end time!")

