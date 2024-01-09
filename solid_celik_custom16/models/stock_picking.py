
from odoo import models, fields, api


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    number_of_packages = fields.Integer(string='Number of Packages', compute="_cal_pacages")

    @api.depends('move_ids')
    def _compute_gross_weight(self):
        for record in self:
            record.weight_gross = sum(move.gross_weight for move in record.move_ids if move.state != 'cancel')

    @api.depends('move_ids')
    def _cal_weight(self):
        for picking in self:
            picking.weight = sum(move.net_weight for move in picking.move_ids if move.state != 'cancel')

    @api.depends('move_ids')
    def _cal_pacages(self):
        for picking in self:
            picking.number_of_packages = sum(int(move.product_packaging_id.name) for move in picking.move_ids if move.state != 'cancel')