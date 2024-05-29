# -*- coding: utf-8 -*-
{
    'name': "Voucher",

    'summary': """
        Tạo nút Voucher cho POS""",

    'description': """
        Tạo nút voucher để xem các chương trình khuyến mãi tại địa điểm bán lẻ của FAHASA
    """,

    'author': "Nhóm 4",

    'category': 'Sales',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['point_of_sale','pos_coupon'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'assets': {
        'point_of_sale.assets':[
                'buttons/static/src/js/**/*',
            'buttons/static/src/xml/**/*',
        ],
        'web.assets_qweb': [
            'buttons/static/src/xml/**/*',
            'buttons/static/src/js/**/*'
        ]
    },
    'license': 'LGPL-3',
}
