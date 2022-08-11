# -*- coding: utf-8 -*-
{
    'name': "Salesperson Name in invoice",

    'summary': """
        Add salesperson name on invoice
        and add place for salesperson and customer.
        """,

    'description': """
        and some feature for invoice
    """,

    'author': "3C",
    'website': "https://th3.company",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.2',

    # any module necessary for this one to work correctly
    'depends': ['base','account'],

    # always loaded
    'data': [
        'views/views.xml',
        'report/report_inv.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        # 'demo/demo.xml',
    ],
}
