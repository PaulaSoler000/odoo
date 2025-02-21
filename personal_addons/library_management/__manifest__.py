


{
    'name': 'Gestión de Biblioteca',
    'version': '1.0',
    'category': 'Educación',
    'summary': 'Módulo para gestionar autores y libros',
    'description': """
        Este módulo permite la gestión de autores y libros en una biblioteca.
    """,
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/author_views.xml',
        'views/book_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}

