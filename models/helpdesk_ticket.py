from odoo import models, fields

class HelpdeskTicket(models.Model):
    _inherit = "helpdesk.ticket"

    hours_estimated = fields.Float(string="Horas Estimadas")
    hours_approved = fields.Float(string="Horas Aprobadas")
