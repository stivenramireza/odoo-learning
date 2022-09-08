# from odoo import http


# class OdooModelAdvanced(http.Controller):
#     @http.route('/odoo_view_advanced/odoo_view_advanced/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/odoo_view_advanced/odoo_view_advanced/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('odoo_view_advanced.listing', {
#             'root': '/odoo_view_advanced/odoo_view_advanced',
#             'objects': http.request.env['odoo_view_advanced.odoo_view_advanced'].search([]),
#         })

#     @http.route('/odoo_view_advanced/odoo_view_advanced/objects/<model("odoo_view_advanced.odoo_view_advanced"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('odoo_view_advanced.object', {
#             'object': obj
#         })
