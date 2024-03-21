{
    'name': "my_hospital",

    'author': "YevdokimovA",
    'website': "https://yevdokimova.com",

    'category': "Customization",
    'license': "OPL-1",
    'version': "17.0.0.0.1",

    'depends': ['base', 'sale'],
    'data': [
        'security/ir.model.access.csv',
        'views/hr_hospital_menus_views.xml',
        'wizard/change_doctor_wizard_views.xml',
        'views/patient_views.xml',
        'views/doctor_views.xml',
        'views/disease_views.xml',
        'views/patient_visits_views.xml',
        'views/diagnosis_views.xml',
        'views/history_change_views.xml',
        'views/doctor_schedule_views.xml',
        'data/disease_data.xml',
        'report/report_doctor.xml',
        'report/report.xml',
    ],
    'demo': [
        'demo/doctor_demo.xml',
        'demo/patient_demo.xml',
        'demo/disease_demo.xml',
    ],

    'installable': True,
    'auto_install': False,
    'application': True,
}
