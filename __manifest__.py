{
    'name': "Darflogin",
    'version': '1.0',
    'depends': ['base',
                'sale',
                'delivery',
                'website',
],
    'author': "Sergey Stepanets",
    'category': 'Application',
    'description': """
    Module that for singup customers only who has tokens
    """,
    'data': [
        'views/singup_settings.xml',
        'views/templates/darf_signup.xml',
        
    ],
}