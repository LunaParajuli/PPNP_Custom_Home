{
    'name': 'PPNPL_Report_Wizard',
    'version': '19.0.1.0.0',
    'summary': 'Salesperson wizard and PDF report',
    'summary': 'Customization for Wizard  and Salesperson total sales PDF Report',
    'author': 'Luna',
    'category': 'Custom',
    'depends': ['base','sale'],
  'data': [
           'security/ir.model.access.csv',
           'wizard/saleperson_wizard.xml',
           'report/report_action.xml',
           'report/report_template.xml',
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}