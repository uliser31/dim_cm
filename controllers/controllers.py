# -*- coding: utf-8 -*-
# from odoo import http


# class DimCm(http.Controller):
#     @http.route('/dim_cm/dim_cm', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/dim_cm/dim_cm/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('dim_cm.listing', {
#             'root': '/dim_cm/dim_cm',
#             'objects': http.request.env['dim_cm.dim_cm'].search([]),
#         })

#     @http.route('/dim_cm/dim_cm/objects/<model("dim_cm.dim_cm"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('dim_cm.object', {
#             'object': obj
#         })
