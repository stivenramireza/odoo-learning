from odoo import models, fields


class Visit(models.Model):
    _name = 'custom_crm.visit'
    _description = 'Visit'

    name = fields.Char(string='Description')
    customer = fields.Char(string='Customer')
    date = fields.Datetime(string='Date')
    type = fields.Selection(
        [('P', 'Present'), ('W', 'WhatsApp'), ('T', 'Telephone')], 
        string='Type',
        required=True
    )
    done = fields.Boolean(string='Done', readonly=True)