from odoo import fields, models


class ClinicVisit(models.Model):
    _inherit = "clinic.visit"

    invoice_id = fields.Many2one("account.move", readonly=True)

    def action_create_invoice(self):
        for visit in self:
            if visit.invoice_id:
                continue
            partner = visit.patient_id.partner_id or self.env["res.partner"].create({
                "name": visit.patient_id.name,
                "phone": visit.patient_id.phone,
            })
            lines = []
            for service in visit.service_ids:
                product = service.product_id
                lines.append((0, 0, {
                    "name": service.name,
                    "product_id": product.id if product else False,
                    "quantity": 1,
                    "price_unit": service.price,
                }))
            move = self.env["account.move"].create({
                "move_type": "out_invoice",
                "partner_id": partner.id,
                "invoice_line_ids": lines,
            })
            visit.invoice_id = move.id
