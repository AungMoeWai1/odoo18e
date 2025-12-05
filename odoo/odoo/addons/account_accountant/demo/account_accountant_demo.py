import time

from odoo import api, models, Command, _


class AccountChartTemplate(models.AbstractModel):
    _inherit = "account.chart.template"

    @api.model
    def _get_demo_data_move(self, company=False):
        move_data = super()._get_demo_data_move(company)
        move_data['demo_invoice_deferred'] = {
            'move_type': 'out_invoice',
            'partner_id': 'base.res_partner_1',
            'invoice_user_id': 'base.user_demo',
            'invoice_date': time.strftime('%Y-01-01'),
            'invoice_line_ids': [
                Command.create({
                    'name': _('Subscription 12 months'),
                    'quantity': 1,
                    'price_unit': 120,
                    'deferred_start_date': time.strftime('%Y-01-01'),
                    'deferred_end_date': time.strftime('%Y-12-31'),
                }),
            ]
        }
        move_data['demo_bill_deferred'] = {
            'move_type': 'in_invoice',
            'partner_id': 'base.res_partner_1',
            'invoice_user_id': 'base.user_demo',
            'invoice_date': time.strftime('%Y-01-01'),
            'invoice_line_ids': [
                Command.create({
                    'name': _('Insurance 12 months'),
                    'quantity': 1,
                    'price_unit': 1200,
                    'deferred_start_date': time.strftime('%Y-01-01'),
                    'deferred_end_date': time.strftime('%Y-12-31'),
                }),
            ]
        }
        return move_data
