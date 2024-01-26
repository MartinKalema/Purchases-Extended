# -*- coding: utf-8 -*-
# from odoo import http


# class PurchaseRfqUpgrade(http.Controller):
#     @http.route('/purchase_rfq_upgrade/purchase_rfq_upgrade', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/purchase_rfq_upgrade/purchase_rfq_upgrade/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('purchase_rfq_upgrade.listing', {
#             'root': '/purchase_rfq_upgrade/purchase_rfq_upgrade',
#             'objects': http.request.env['purchase_rfq_upgrade.purchase_rfq_upgrade'].search([]),
#         })

#     @http.route('/purchase_rfq_upgrade/purchase_rfq_upgrade/objects/<model("purchase_rfq_upgrade.purchase_rfq_upgrade"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('purchase_rfq_upgrade.object', {
#             'object': obj
#         })

