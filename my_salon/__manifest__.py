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
        'views/menu.xml',
        'views/client.xml',
        'views/master.xml'

    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
