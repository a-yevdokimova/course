{
    'name': "my_salon",

    'author': "YevdokimovA",
    'website': "https://yevdokimova.com",

    'category': "Customization",
    'license': "OPL-1",
    'version': "17.0.0.0.1",

    'depends': ['base', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'data/sequence.xml',
        'views/menu_views.xml',
        'views/client_views.xml',
        'views/master_views.xml',
        'views/service_views.xml',
        # 'views/appointment_views.xml',
        # 'views/product_views.xml',

    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
