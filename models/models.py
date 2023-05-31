# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class dim_cm(models.Model):
#     _name = 'dim_cm.dim_cm'
#     _description = 'dim_cm.dim_cm'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
