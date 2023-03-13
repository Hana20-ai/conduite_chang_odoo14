# -*- coding: utf-8 -*-
{
    'name': "Registre Partenaires",

    'summary': """
        Gestion des parties prenantes dans la démarche de la conduite de changement""",

    'description': """
        Gestion des parties prenantes dans la demarche de la conduite de changement
    """,
    'sequence': -120,	
    'author': "ESI",
    'website': "https://www.esi.dz",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Productivity',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['project','base'],

    # always loaded
    'data': [
	'security/ir.model.access.csv',
	'security/security.xml',
        'data/data.xml',
        'views/templates.xml',
        'views/partieprenante.xml',
	'reports/reports.xml',
	
	

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
