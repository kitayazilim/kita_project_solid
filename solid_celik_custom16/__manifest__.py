# Copyright 2023 Kıta Yazılım
# License LGPLv3 or later (https://www.gnu.org/licenses/lgpl-3.0).

{
    'name': 'Solid Celik Custom16',
    'summary': """Solid Çelik custom geliştirmeleri v16""",
    'description': """Solid Çelik custom geliştirmeleri v16""",
    'version': '16.0.1',
    'license': 'LGPL-3',
    'author': 'Kıta Yazılım',
    'website': 'kitayazilim.com.tr',
    'depends': ['sale', 'stock', 'stock_foreign_trade'],
    'data': [
        'views/product_attribute.xml',
        'views/sale_order.xml',
        'views/stock_picking.xml',
        'reports/report_sale_order_document.xml',
    ],
    'demo': [
    ],
}
