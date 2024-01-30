# -*- coding: utf-8 -*-
{
    'name': "Purchases",
    'summary': "Missing functionalities for the Purchase application/module.",
    'description': """
    Creating a customization such that one RFQ can be assigned to multiple vendors at the model level, 
    implementing the process of receiving bids and selecting the winning bidder
    """,
    'author': "Kalema",
    'website': "https://github.com/MartinKalema/",
    'category': 'Uncategorized',
    'sequence': -100,
    'version': '0.1',
    'depends': ['base', 'mail', 'purchase'],
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
    'application': True,
    'installable': True,
    'auto_install': False,
    'assets': {},
    'license': 'LGPL-3',
}

