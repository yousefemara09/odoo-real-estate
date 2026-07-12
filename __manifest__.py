{
    'name': 'App one',
    'author': "Yousef Ibrahim",
    'version': '17.0.0.1.0',
    'category': '',
    'depends': [
        'base', 'sale_management', 'account' , 'mail'
    ],
    'data': [
    'security/security.xml',
    'security/ir.model.access.csv',
    'data/sequance.xml',
    'data/data.xml',
    'views/base_menu.xml',
    'views/property_view.xml',
    'views/owner_view.xml',
    'views/tags_view.xml',
    'views/sale_order_view.xml',
    'views/res_partner_view.xml',
    'views/property_history_view.xml',
    'views/account_move_view.xml',
    'wizard/change_widzard_state.xml',
    'reports/property_report.xml'
    ],
    'assets': {
    'web.assets_backend': [
        'app_one/static/src/css/property.css',
        'app_one/static/src/componants/ListView/listView.js',
        'app_one/static/src/componants/ListView/listView.css',
        'app_one/static/src/componants/ListView/listView.xml',
        'app_one/static/src/componants/formView/formView.xml',
        # 'app_one/static/src/componants/formView/formView.css',
        'app_one/static/src/componants/formView/formView.js',

    ],
    'web.report_assets_common': [
        'app_one/static/src/fonts/Ole-Regular.ttf',
    ],

    },
    'application': True,
    'license': 'LGPL-3',
}