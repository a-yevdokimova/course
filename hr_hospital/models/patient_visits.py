import logging
from odoo import fields, models, api
from odoo.exceptions import ValidationError

_logger = logging.getLogger(__name__)


class PatientsVisit(models.Model):
    _name = "patient.visits"
    _description = "Patients Visits"

    visit_date = fields.Datetime()
    doctor_id = fields.Many2one(comodel_name='doctor')
    patient_id = fields.Many2one(comodel_name='patient')
    diagnosis_ids = fields.One2many('diagnosis', 'visit_id', string='Diagnoses')
    active = fields.Boolean(default=True)

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

    # def write(self, vals):
    #     if 'active' in vals and not vals['active']:
    #         visits_with_diagnoses = self.filtered(lambda visit: visit.diagnosis_ids)
    #         if visits_with_diagnoses:
    #             raise ValidationError("You cannot archive visits with diagnoses.")
    #     return super(PatientsVisit, self).write(vals)
