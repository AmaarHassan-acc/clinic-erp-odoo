from odoo import fields, models


class ClinicRoom(models.Model):
    _name = "clinic.room"
    _description = "Clinic Room"
    _order = "name"

    name = fields.Char(required=True)
    department = fields.Char()
    active = fields.Boolean(default=True)
    notes = fields.Text()
