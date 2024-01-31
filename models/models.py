# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Order(models.Model):
    _inherit = 'purchase.order'
    _description = 'Order'
    vendor_ids = fields.One2many('res.partner', 'vendor_id', string='vendors')


class Partner(models.Model):
    _inherit = 'res.partner'
    _description = 'Partner'
    vendor_id = fields.Many2one('purchase.order', string='vendor')


