from odoo import fields, models


class ClinicService(models.Model):
    _name = "clinic.service"
    _description = "Clinic Service / Price List"
    _order = "department, name"

    name = fields.Char(required=True)
    department = fields.Char()
    service_type = fields.Selection([
        ("consultation", "Consultation"), ("lab", "Lab"), ("procedure", "Procedure"),
        ("radiology", "Radiology"), ("other", "Other"),
    ], default="consultation")
    price = fields.Monetary(required=True, default=0.0)
    taxable = fields.Boolean(default=True)
    product_id = fields.Many2one("product.product", string="Related Product")
    currency_id = fields.Many2one("res.currency", default=lambda self: self.env.company.currency_id, required=True)
    active = fields.Boolean(default=True)
