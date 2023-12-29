# Copyright 2023 Kıta Yazılım
# License LGPLv3 or later (https://www.gnu.org/licenses/lgpl-3.0).

from odoo import _, api, fields, models


class SaleOrder(models.Model):

    _inherit = "sale.order"

    order_type = fields.Selection(selection=[
        ("normal", "Normal"),
        ("ceramic", "Seramik"),
        ("steel", "Çelik"),
    ], string='Sipariş Türü', copy=False)