#!/usr/bin/python -u

from pyoms import orderManager

om = orderManager.OrderManager()


orderDetails = {'symbol': 'IBM', 'side': 'Buy', 'quantity': 100, 'price': 245.09, 'destination': 'XNYS'}
om.book.orders[no].set_properties_dict(orderDetails)


