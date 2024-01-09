# Copyright 2023 Kıta Yazılım
# License LGPLv3 or later (https://www.gnu.org/licenses/lgpl-3.0).

from odoo import _, api, fields, models
from odoo.exceptions import RedirectWarning, UserError, ValidationError


class StockMove(models.Model):

    _inherit = "stock.move"

    gross_weight = fields.Float("Gross Weight")
    net_weight = fields.Float("Net Weight")

    @api.constrains('gross_weight')
    def _check_gross_weight(self):
        for record in self:
            if record.gross_weight <= 0:
                raise ValidationError(_("Brüt Ağırlığı girilmeyen satır(lar) var!"))
            
    @api.constrains('net_weight')
    def _check_net_weight(self):
        for record in self:
            if record.net_weight <= 0:
                raise ValidationError(_("Net Ağırlığı girilmeyen satır(lar) var!"))
