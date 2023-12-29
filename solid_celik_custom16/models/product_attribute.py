# Copyright 2023 Kıta Yazılım
# License LGPLv3 or later (https://www.gnu.org/licenses/lgpl-3.0).

from odoo import _, api, fields, models


class ProductAttribute(models.Model):

    _inherit = "product.attribute"

    show_on_report = fields.Boolean('Raporlarda Göster')