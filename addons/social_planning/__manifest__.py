{
    'name': 'Social planning',
    'version': '14.0.1.0.0',
    'website': 'https://github.com/skeller1/iclaas',
    'category': 'Services',
    'sequence': 50,
    'summary': 'Organize and plan your shifts',
    'depends': [
        'hr',
        'hr_timesheet',
        'web',
    ],
    'description': "",
    'data': [
        # 'security/project_security.xml',
        'security/ir.model.access.csv',
        'views/social_planning_views.xml',
    ],
    # 'demo': ['data/social_planning_demo.xml'],
    #'qweb': ['static/src/xml/social_planning_templates.xml'],
    'test': [
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
