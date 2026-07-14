from odoo import fields, models


class ClinicPatient(models.Model):
    _name = "clinic.patient"
    _description = "Clinic Patient"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _order = "name"

    name = fields.Char(required=True, tracking=True)
    phone = fields.Char(tracking=True)
    national_id = fields.Char(string="National ID", tracking=True)
    gender = fields.Selection([("male", "Male"), ("female", "Female"), ("other", "Other")])
    date_of_birth = fields.Date(string="Date of Birth")
    notes = fields.Text()
    partner_id = fields.Many2one("res.partner", string="Related Contact")
    active = fields.Boolean(default=True)
