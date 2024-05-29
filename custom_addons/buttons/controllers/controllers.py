# -*- coding: utf-8 -*-
# from odoo import http


# class Buttons(http.Controller):
#     @http.route('/buttons/buttons', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/buttons/buttons/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('buttons.listing', {
#             'root': '/buttons/buttons',
#             'objects': http.request.env['buttons.buttons'].search([]),
#         })

#     @http.route('/buttons/buttons/objects/<model("buttons.buttons"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('buttons.object', {
#             'object': obj
#         })
