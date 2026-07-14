from odoo import fields, models


class ClinicStaff(models.Model):
    _name = "clinic.staff"
    _description = "Clinic Medical Staff"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _order = "name"

    name = fields.Char(required=True, tracking=True)
    user_id = fields.Many2one("res.users", string="Odoo User")
    staff_type = fields.Selection([
        ("medical", "Medical"), ("nursing", "Nursing"), ("reception", "Reception"),
        ("administration", "Administration"), ("finance", "Finance"),
        ("laboratory", "Laboratory"), ("radiology", "Radiology"), ("other", "Other"),
    ], default="medical", required=True, tracking=True)
    position = fields.Char(tracking=True)
    main_role = fields.Selection([
        ("clinical", "Clinical"), ("reception", "Reception"), ("operations", "Operations"),
        ("billing", "Billing"), ("support", "Support"), ("management", "Management"),
    ], default="clinical", tracking=True)
    department = fields.Char(tracking=True)
    specialty = fields.Char(string="Specialty / Skill")
    gender = fields.Selection([("male", "Male"), ("female", "Female"), ("other", "Other")])
    languages = fields.Char(default="Arabic, English")
    phone = fields.Char()
    email = fields.Char()
    license_no = fields.Char(string="License / Employee No.")
    room_id = fields.Many2one("clinic.room")
    notes = fields.Text()
    active = fields.Boolean(default=True)
