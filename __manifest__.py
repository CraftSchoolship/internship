{
    'name':'Movie Module',
    'author':'Ithar',
    'category': 'Tools',
    'description': """
    Movie Module test
    """,
    'depends': ['base', 'website'],
    'data': [
        'views/movie.xml',
        'security/ir.model.access.csv',
        'views/templates.xml',

     ],
    
    'installable': True,
    'application': True,
}