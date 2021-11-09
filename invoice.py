# The COPYRIGHT file at the top level of
# this repository contains the full copyright notices and license terms.
from trytond.model import ModelView, ModelSQL, fields
from trytond.pool import PoolMeta
from trytond.pyson import Eval
from trytond.transaction import Transaction


class CancelReason(ModelSQL, ModelView):
    'Invoice Cancel Reason'
    __name__ = 'account.invoice.cancel.reason'
    name = fields.Char('Name', translate=True)


class Invoice(metaclass=PoolMeta):
    __name__ = 'account.invoice'
    cancel_reason = fields.Many2One('account.invoice.cancel.reason',
        'Cancel Reason', states={
            'required': ((Eval('state') == 'cancelled')
                & ~Eval('context', {}).get('invoice_force_cancel', False)),
            'readonly': Eval('state') == 'cancelled',
            },
        depends=['state'])
    cancel_description = fields.Text('Cancel Description',
        states={
            'required': ((Eval('state') == 'cancelled')
                & ~Eval('context', {}).get('invoice_force_cancel', False)),
            'readonly': Eval('state') == 'cancelled',
            },
        depends=['state'])

    @classmethod
    def delete(cls, invoices):
        with Transaction().set_context(invoice_force_cancel=True):
            super(Invoice, cls).delete(invoices)
