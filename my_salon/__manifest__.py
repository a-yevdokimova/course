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
        'views/appointment_views.xml',
        'views/product_views.xml',
        'views/provider_views.xml'

    ],

    'demo': [
        'demo/appointment_demo.xml',
        'demo/client_demo.xml',
        'demo/master_demo.xml',
        'demo/product_demo.xml',
        'demo/provider_demo.xml',
        'demo/service_demo.xml'
    ],

    'installable': True,
    'auto_install': False,
    'application': True,
}
