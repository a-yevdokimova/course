{
    'name': "my_hospital",

    'author': "YevdokimovA",
    'website': "https://yevdokimova.com",

    'category': "Customization",
    'license': "OPL-1",
    'version': "17.0.0.0.1",

    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/menu_views.xml',
        'views/patient_views.xml',
        'views/doctor_views.xml',
        'views/disease_views.xml',
        'views/patient_visits_views.xml',
        'views/diagnosis_views.xml',
        'data/disease_data.xml',
    ],
    'demo': [
        'demo/doctor_demo.xml',
        'demo/patient_demo.xml',
    ],

    'installable': True,
    'auto_install': False,
    'application': True,
}
