# -*- coding: utf-8 -*-
# from odoo import http


# class Ciclos(http.Controller):
#     @http.route('/ciclos/ciclos', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ciclos/ciclos/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('ciclos.listing', {
#             'root': '/ciclos/ciclos',
#             'objects': http.request.env['ciclos.ciclos'].search([]),
#         })

#     @http.route('/ciclos/ciclos/objects/<model("ciclos.ciclos"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ciclos.object', {
#             'object': obj
#         })

