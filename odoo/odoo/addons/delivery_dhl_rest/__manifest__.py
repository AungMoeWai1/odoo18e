# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': "DHL Express Shipping",
    'description': "Send your shippings through DHL and track them online",
    'category': 'Inventory/Delivery',
    'version': '1.0',
    'application': True,
    'depends': ['stock_delivery', 'mail'],
    'data': [
        'data/delivery_dhl_data.xml',
        'views/delivery_dhl_view.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
    'license': 'OEEL-1',
}
