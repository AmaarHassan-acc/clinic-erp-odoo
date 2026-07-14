from odoo import api, fields, models


class ClinicVisit(models.Model):
    _name = "clinic.visit"
    _description = "Clinic Visit"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _order = "visit_date desc, visit_time desc"

    name = fields.Char(default="New", copy=False, readonly=True)
    appointment_id = fields.Many2one("clinic.appointment")
    patient_id = fields.Many2one("clinic.patient", required=True, tracking=True)
    doctor_id = fields.Many2one("clinic.staff", required=True, tracking=True)
    department = fields.Char(related="doctor_id.department", store=True, readonly=False)
    room_id = fields.Many2one("clinic.room")
    visit_date = fields.Date(default=fields.Date.context_today, required=True)
    visit_time = fields.Float()
    service_ids = fields.Many2many("clinic.service", string="Services")
    state = fields.Selection([
        ("waiting", "Waiting"), ("with_doctor", "With Doctor"), ("completed", "Completed"), ("cancelled", "Cancelled"),
    ], default="waiting", tracking=True)
    diagnosis = fields.Text()
    clinical_notes = fields.Text()

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get("name", "New") == "New":
                vals["name"] = self.env["ir.sequence"].next_by_code("clinic.visit") or "New"
        return super().create(vals_list)

    def action_with_doctor(self):
        self.write({"state": "with_doctor"})

    def action_complete(self):
        self.write({"state": "completed"})

    def action_cancel(self):
        self.write({"state": "cancelled"})
