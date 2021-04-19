{
    'name': 'custom_crm',
    'summary': 'Module to manage visits',
    'description': 'Module to manage visits...',
    'author': 'Stiven Ramírez Arango',
    'website': 'http://www.odoo.com',
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': ['base', 'sale_management'],
    'data': [
        'views/views.xml',
        'views/templates.xml',
        'reports/visit.xml'
    ],
    'demo': [
        'demo/demo.xml'
    ]
}