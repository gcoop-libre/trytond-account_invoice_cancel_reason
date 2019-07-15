# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.pool import Pool
from . import invoice


def register():
    Pool.register(
        invoice.CancelReason,
        invoice.Invoice,
        module='account_invoice_cancel_reason', type_='model')
