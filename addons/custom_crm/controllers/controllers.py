from odoo import http
import json


class VisitController(http.Controller):

    @http.route('/api/visits', auth='public', method=['GET'], csrf=False)
    def get_visits(self, **kwargs):
        try:
            visits = http.request.env['custom_crm.visit'].sudo().search_read([], ['id', 'name', 'customer', 'done'])
            res = json.dumps(visits, ensure_ascii=False).encode('utf-8')
            return http.Response(res, content_type='application/json;charset=utf-8', status=200)
        except Exception as e:
            return http.Response(json.dumps({'error': e}), content_type='application/json;charset=utf-8', status=505)
