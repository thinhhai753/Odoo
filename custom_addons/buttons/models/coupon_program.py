# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class buttons(models.Model):
#     _name = 'buttons.buttons'
#     _description = 'buttons.buttons'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
from odoo import models, fields, api
 
class Coupon_program(models.Model):
   _inherit = 'coupon.program'