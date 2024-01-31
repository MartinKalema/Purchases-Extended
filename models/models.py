# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Purchase(models.Model):
    _inherit = 'purchase.order'
    # fields
    date = fields.Date(string='Date')

