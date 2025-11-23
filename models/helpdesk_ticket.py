from odoo import models, fields

class HelpdeskTicket(models.Model):
    _inherit = "helpdesk.ticket"

    hours_estimated = fields.Float(string="Estimated Time (Hours)")
    hours_approved = fields.Float(string="Approved Time (Hours)")
    approved_cost_usd = fields.Float(string="Approved Cost (USD)")
