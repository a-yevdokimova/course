from odoo import api, fields, models
from odoo.exceptions import ValidationError
from datetime import date
from datetime import datetime
from dateutil.relativedelta import relativedelta

class Appointment(models.Model):
    _name = "appointment"
    _description ="Appointment Records"

    visit_status = fields.Selection([('scheduled', 'Scheduled'),
                                     ('completed', 'Completed'),
                                     ('cancelled', 'Cancelled')],
                                    default='scheduled')
    client_id = fields.Many2one('client', required=True)
    master_id = fields.Many2one('master', required=True)
    service_id = fields.Many2one('my_service', required=True)
    start_time = fields.Datetime()
    end_time = fields.Datetime(compute='_compute_end_time')

    @api.constrains('start_time', 'end_time')
    def _check_time_range(self):
        for record in self:
            if record.start_time >= record.end_time:
                raise ValidationError("Start time must be earlier than end time!")
    @api.depends('service_id','start_time')
    def _compute_end_time(self):
        for rec in self:
            rec.end_time = rec.start_time + relativedelta(hours=rec.service_id.duration)



