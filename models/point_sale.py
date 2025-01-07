from odoo import fields, models

class PointSale(models.Model):
    _inherit = 'res.partner'

    language = fields.Char(string='Language')


