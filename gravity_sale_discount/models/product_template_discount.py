from odoo import api, fields, models, tools, _
from odoo.exceptions import ValidationError


class ProductProduct(models.Model):
    _inherit = "product.template"

    discount_percentage = fields.Float(help='This field is used to define the product discount as a percentage for online sale')

class SaleOrder(models.Model):
    _inherit = "sale.order"

    ## update the discount percentage when create sale_order
    def _prepare_order_line_values(self, product_id, quantity, **kwargs):
        self.ensure_one()
        product = self.env['product.product'].browse(product_id)
        res = super()._prepare_order_line_values(product_id, quantity, **kwargs)
        res.update({
            'discount':product.discount_percentage
        })
        return res

    ## updat the price when change the quantity
    def _prepare_order_line_update_values(
            self, order_line, quantity, linked_line_id=False, **kwargs
    ):
        self.ensure_one()
        order_line_obj = self.env['sale.order.line'].browse(order_line)
        res = super()._prepare_order_line_update_values(order_line, quantity, linked_line_id=False, **kwargs)
        res.update({
            'discount': order_line.product_id.discount_percentage
        })
        return res

    def _get_update_prices_lines(self): ## Fix the recompute method for discount feature by overriding
        """ Hook to exclude specific lines which should not be updated based on price list recomputation """
        return self.order_line.filtered(lambda line: not line.display_type and line.discount ==0.0)

