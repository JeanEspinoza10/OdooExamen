from odoo import api, fields, models

class SalesChannel(models.Model):
    _name="sales.channel"
    _description="Sales Channel"

    name = fields.Char(string='Name', required=True)
