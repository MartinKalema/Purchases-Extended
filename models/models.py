# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Order(models.Model):
    _inherit = 'purchase.order'
    _description = 'Order'
    relation_ids = fields.One2many('res.partner', 'relation_id', string='relations')


class Partner(models.Model):
    _inherit = 'res.partner'
    _description = 'Res Partner'
    relation_id = fields.Many2one('purchase.order', string='relation')


