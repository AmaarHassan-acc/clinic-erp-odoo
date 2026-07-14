from odoo import api, fields, models


class ClinicPrescription(models.Model):
    _name = "clinic.prescription"
    _description = "Clinic Prescription"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _order = "date desc, name desc"

    name = fields.Char(default="New", copy=False, readonly=True)
    visit_id = fields.Many2one("clinic.visit")
    patient_id = fields.Many2one("clinic.patient", required=True)
    doctor_id = fields.Many2one("clinic.staff", required=True)
    date = fields.Date(default=fields.Date.context_today, required=True)
    diagnosis = fields.Text()
    notes = fields.Text()
    line_ids = fields.One2many("clinic.prescription.line", "prescription_id")

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get("name", "New") == "New":
                vals["name"] = self.env["ir.sequence"].next_by_code("clinic.prescription") or "New"
        return super().create(vals_list)


class ClinicPrescriptionLine(models.Model):
    _name = "clinic.prescription.line"
    _description = "Clinic Prescription Line"

    prescription_id = fields.Many2one("clinic.prescription", required=True, ondelete="cascade")
    medicine = fields.Char(required=True)
    dosage = fields.Char()
    frequency = fields.Char()
    duration = fields.Char()
