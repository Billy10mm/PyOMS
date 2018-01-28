#!/usr/bin/python -u

from pyoms import orderManager

om = orderManager.OrderManager()
om.create_book('BILL')

orderDetails = {'symbol': 'IBM', 'side': 'Buy', 'quantity': 100, 'price': 245.09, 'destination': 'XNYS'}
oid = om.books['BILL'].create_order()
om.books['BILL'].orders[oid].set_properties_dict(orderDetails)

print om.books['BILL'].orders[oid].get_properties_dict()

