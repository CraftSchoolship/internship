{
    'name': "Movies",
    'author': "Mor Mbathie",
    'website': "www.odootest.com",
    'summary': "odoo 16 Development",
    'category': "Tools",
    'depends': ['base'],
    'data': [
        'views/movie_view.xml',  # Assurez-vous que le nom du fichier est correct
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
