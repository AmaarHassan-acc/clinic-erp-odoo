from odoo import api, fields, models


class ClinicAppointment(models.Model):
    _name = "clinic.appointment"
    _description = "Clinic Appointment"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _order = "appointment_date desc, appointment_time desc"

    name = fields.Char(default="New", copy=False, readonly=True)
    patient_id = fields.Many2one("clinic.patient", required=True, tracking=True)
    doctor_id = fields.Many2one("clinic.staff", required=True, tracking=True)
    department = fields.Char(related="doctor_id.department", store=True, readonly=False)
    room_id = fields.Many2one("clinic.room", tracking=True)
    appointment_date = fields.Date(required=True, tracking=True)
    appointment_time = fields.Float(required=True, tracking=True)
    service_ids = fields.Many2many("clinic.service", string="Services")
    concerns = fields.Text(string="Patient Concerns")
    state = fields.Selection([
        ("booked", "Booked"), ("waiting", "Waiting"), ("with_doctor", "With Doctor"),
        ("completed", "Completed"), ("cancelled", "Cancelled"),
    ], default="booked", tracking=True)
    visit_id = fields.Many2one("clinic.visit", readonly=True)

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get("name", "New") == "New":
                vals["name"] = self.env["ir.sequence"].next_by_code("clinic.appointment") or "New"
        return super().create(vals_list)

    def action_send_to_queue(self):
        self.write({"state": "waiting"})

    def action_cancel(self):
        self.write({"state": "cancelled"})
