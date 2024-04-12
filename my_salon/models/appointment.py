from odoo import api, fields, models, _
from odoo.exceptions import ValidationError
from dateutil.relativedelta import relativedelta


class Appointment(models.Model):
    """
        A model representing an appointment in a beauty salon.
    """

    _name = "appointment"
    _description = "Appointment Records"
    _rec_name = "display_name"

    visit_status = fields.Selection([('scheduled', 'Scheduled'),
                                     ('completed', 'Completed'),
                                     ('cancelled', 'Cancelled')],
                                    default='scheduled')
    client_id = fields.Many2one('client', required=True)
    master_id = fields.Many2one('master', required=True)
    service_id = fields.Many2one('my_service', required=True)
    start_time = fields.Datetime()
    end_time = fields.Datetime(compute='_compute_end_time')
    display_name = fields.Char(compute='_compute_display_name', store=True,
                               readonly=True)

    @api.constrains('start_time', 'end_time')
    def _check_time_range(self):
        """
        Validates that the appointment's start time is before its end time.
        Raises:
        ValidationError: If the start time is not earlier than the end time.
        """
        for record in self:
            if record.start_time >= record.end_time:
                raise ValidationError(_("Start time must be earlier than end time"))

    @api.depends('service_id', 'start_time')
    def _compute_end_time(self):
        """
        Computes the end time of the appointment based on the service duration.
        The end time is determined by adding the duration of the selected service to the start time.
        """

        for rec in self:
            if rec.start_time and rec.service_id and rec.service_id.duration:
                rec.end_time = rec.start_time + relativedelta(hours=rec.service_id.duration)
            else:
                rec.end_time = False

    @api.depends('client_id.name', 'service_id.name')
    def _compute_display_name(self):
        for record in self:
            client_name = record.client_id.name if record.client_id else ''
            service_name = record.service_id.name if record.service_id else ''
            # Создаем строку с именем клиента и названием услуги
            record.display_name = f'{client_name} - {service_name}'
