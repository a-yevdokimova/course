import logging
from odoo import fields, models, api, _
from odoo.exceptions import ValidationError

_logger = logging.getLogger(__name__)


class PatientsVisit(models.Model):
    _name = "patient.visits"
    _description = "Patients Visits"

    visit_status = fields.Selection([('scheduled', 'Scheduled'),
                               ('completed', 'Completed'),
                               ('cancelled', 'Cancelled')],
                                default='scheduled')
    visit_date = fields.Datetime(string="Planned date", help='The planned date and time of the visit')
    visit_done_date = fields.Datetime(string="Done date", help='Date and time when the visit took place')
    doctor_id = fields.Many2one(comodel_name='doctor')
    patient_id = fields.Many2one(comodel_name='patient')
    diagnosis_ids = fields.One2many('diagnosis', 'visit_id', string='Diagnoses')
    active = fields.Boolean(default=True)
    confirmation = fields.Boolean(string='Confirmation from doctor-mentor')
    # appointment_id = fields.Many2one('doctor.schedule')
    # is_appointment_done = fields.Boolean(string="Is the appointment done?")

    @api.constrains('visit_date', 'doctor_id')
    def _check_unique_doctor_visit(self):
        for record in self:
            if record.visit_date and record.doctor_id:
                existing_record = self.env['patient.visits'].search([
                    ('visit_date', '=', record.visit_date),
                    ('doctor_id', '=', record.doctor_id.id),
                    ('id', '!=', record.id),
                ])
                if existing_record:
                    raise ValidationError('A visit to this doctor on this date already exists!')

    def write(self, vals):
        if 'visit_date' in vals or 'doctor_id' in vals:
            for visits in self:
                if visits.visit_date and visits.visit_date < fields.Datetime.now():
                    raise ValidationError("You cannot change visit date/time or doctor for a visit that has already occurred!")
        if 'active' in vals and not vals['active']:
            visits_with_diagnoses = self.filtered(lambda visit: visit.diagnosis_ids)
            if visits_with_diagnoses:
                raise ValidationError("You cannot archive visits with diagnoses.")
        return super(PatientsVisit, self).write(vals)

    def unlink(self):
        visits_with_diagnoses = self.filtered(lambda visit: visit.diagnosis_ids)
        if visits_with_diagnoses:
            raise ValidationError("You cannot delete visits with diagnoses.")
        return super(PatientsVisit, self).unlink()

    @api.depends('patient_id', 'doctor_id')
    def _compute_display_name(self):
        for rec in self:
            rec.display_name = "%s (%s)" % (rec.patient_id.name, rec.doctor_id.name)

    # def write(self, vals):
    #     if 'active' in vals and not vals['active']:
    #         visits_with_diagnoses = self.filtered(lambda visit: visit.diagnosis_ids)
    #         if visits_with_diagnoses:
    #             raise ValidationError("You cannot archive visits with diagnoses.")
    #     return super(PatientsVisit, self).write(vals)
