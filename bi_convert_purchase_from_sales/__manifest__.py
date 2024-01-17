# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

{
    'name' : "Siparişten Satınalma Oluşturma",
    'version' : "16.0.0.2",
    'category' : "Purchases",
    'license': 'OPL-1',
    'summary': 'Bu uygulama siparişten manuel satınalma siparişi oluşturur',
    'description' : """
        Convert Purchase from Sales Order
        Convert Purchases from Sales Order
        Convert Purchase order from Sales Order
        Convert Purchases order from Sales Order

        create Purchase from Sales Order
        create Purchases from Sales Order
        create Purchase order from Sales Order
        create Purchases order from Sales Order


        Add Purchase from Sales Order
        Add Purchases from Sales Order
        ADD Purchase order from Sales Order
        ADD Purchases order from Sales Order

     """,
    'author' : "BrowseInfo",
    'website'  : "https://www.browseinfo.com",
    'depends'  : [ 'base','sale_management','purchase'],
    'data'     : [  'security/ir.model.access.csv',
                    'wizard/purchase_order_wizard_view.xml',
                    'views/inherit_sale_order_view.xml',
            ],      
    'installable' : True,
    'application' :  False,
    "images":['static/description/Banner.gif'],
    'live_test_url':'https://youtu.be/wS4f9hEABxY',
}
