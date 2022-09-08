# -*- coding: utf-8 -*-
# from odoo import http


# class OdooModelAdvanced(http.Controller):
#     @http.route('/odoo_model_advanced/odoo_model_advanced/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/odoo_model_advanced/odoo_model_advanced/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('odoo_model_advanced.listing', {
#             'root': '/odoo_model_advanced/odoo_model_advanced',
#             'objects': http.request.env['odoo_model_advanced.odoo_model_advanced'].search([]),
#         })

#     @http.route('/odoo_model_advanced/odoo_model_advanced/objects/<model("odoo_model_advanced.odoo_model_advanced"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('odoo_model_advanced.object', {
#             'object': obj
#         })
