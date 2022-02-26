# -*- coding: utf-8 -*-
# from odoo import http


# class FichasAutos(http.Controller):
#     @http.route('/fichas_autos/fichas_autos', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/fichas_autos/fichas_autos/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('fichas_autos.listing', {
#             'root': '/fichas_autos/fichas_autos',
#             'objects': http.request.env['fichas_autos.fichas_autos'].search([]),
#         })

#     @http.route('/fichas_autos/fichas_autos/objects/<model("fichas_autos.fichas_autos"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('fichas_autos.object', {
#             'object': obj
#         })
