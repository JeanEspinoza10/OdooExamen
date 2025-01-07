# -*- coding: utf-8 -*-
# from odoo import http


# class Pruebatecnica(http.Controller):
#     @http.route('/pruebatecnica/pruebatecnica', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/pruebatecnica/pruebatecnica/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('pruebatecnica.listing', {
#             'root': '/pruebatecnica/pruebatecnica',
#             'objects': http.request.env['pruebatecnica.pruebatecnica'].search([]),
#         })

#     @http.route('/pruebatecnica/pruebatecnica/objects/<model("pruebatecnica.pruebatecnica"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('pruebatecnica.object', {
#             'object': obj
#         })

