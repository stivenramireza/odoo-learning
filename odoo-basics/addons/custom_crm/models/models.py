from odoo import models, fields, api

import datetime
import logging as logger

logger.basicConfig(level=logger.INFO)


class Visit(models.Model):
    _name = 'custom_crm.visit'
    _description = 'Visit'

    name = fields.Char(string='Description')
    customer = fields.Many2one(string='Customer', comodel_name='res.partner')
    date = fields.Datetime(string='Date')
    type = fields.Selection(
        [('P', 'Present'), ('W', 'WhatsApp'), ('T', 'Telephone')], 
        string='Type',
        required=True
    )
    done = fields.Boolean(string='Done', readonly=True)
    image = fields.Binary(string='Image')

    def toggle_state(self):
        self.done = not self.done

    def f_create(self):
        visit = {
            'name': 'ORM test',
            'customer': 1,
            'date': str(datetime.date(2020, 8, 6)),
            'type': 'P',
            'done': False
        }
        logger.info(visit)
        self.env['custom_crm.visit'].create(visit)

    def f_search_update(self):
        visit = self.env['custom_crm.visit'].search([('name', '=', 'ORM test')])
        logger.info('search()', visit, visit.name)

        visit_b = self.env['custom_crm.visit'].browse([2])
        logger.info('browse()', visit_b, visit_b.name)

        visit.write({
            'name': 'ORM test write'
        })

    def f_delete(self):
        visit = self.env['custom_crm.visit'].browse([2])
        visit.unlink


class VisitReport(models.AbstractModel):
    _name='report.custom_crm.report_visit_card'

    @api.model
    def _get_report_values(self, docids, data=None):
        report_obj = self.env['ir.actions.report']
        report = report_obj._get_report_from_name('custom_crm.report_visit_card')
        return {
            'doc_ids': docids,
            'doc_model': self.env['custom_crm.visit'],
            'docs': self.env['custom_crm.visit'].browse(docids)
        }


class CustomSaleOrder(models.Model):
    _inherit = 'sale.order'

    zone = fields.Selection(
        [('N', 'North'), ('C', 'Center'), ('S', 'South')],
        string='Commercial zone'
    )