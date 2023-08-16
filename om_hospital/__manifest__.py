# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


{
    'name': 'Hospital Management update',
    'version': '1.0.0',
    'category': 'Hospital',
    'author': 'Dhvani',
    'sequence': -100,
    'summary': 'Hospital management system',
    'description': """ Hospital management system""",
    'depends': ['mail', 'product'],
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/patient.xml',
        'views/Female_patient.xml',
        'views/appointment_view.xml',
        'views/patient_tag_view.xml',

    ],
    'demo': [],
    'license': 'LGPL-3',
    'application': 'True',
    'installable': True,
    'auto_install': False,
    'assets': {}
}
