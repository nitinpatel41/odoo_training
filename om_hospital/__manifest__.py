{
    'name' : "Hospital Management",
    'version' : "1.0.0",
    'author' : "Nitin Patel",
    'depends': ['mail'],
    'license': "LGPL-3",
    'sequence': -100,
    'category': 'Hospital',
    'data': [
        'security/ir.model.access.csv',
        'views/action.xml',
        'views/menu.xml',
        'views/patient_view.xml',
        'views/appointment_view.xml'

    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}