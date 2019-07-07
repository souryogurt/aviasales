# -*- coding: utf-8 -*-
"""Module that provides API to partner service"""

from xml.etree import ElementTree as ET
from pkg_resources import resource_filename

__all__ = ['fetch_tickets']


async def fetch_tickets(tickets_type):
    """Make call to partner API and return list of tickets."""
    # In case of actual service, here we can make real HTTP request, but right
    # now we are just using predefined response.
    filename = 'RS_ViaOW.xml' if tickets_type == 'oneway' else 'RS_Via-3.xml'
    fullname = resource_filename('aviasales', filename)
    return parse_tickets(ET.parse(fullname))


def parse_tickets(xml):
    """Parse parther's response and return list of tickets."""
    tickets = list()
    for priced_flight in xml.findall('.//PricedItineraries/Flights'):
        tickets.append({
            'type': get_ticket_type(priced_flight),
        })
    return tickets


def get_ticket_type(ticket):
    """Parse ticket and return ticket type either 'oneway' or 'roundtrip'."""
    if not ticket.find('.//ReturnPricedItinerary'):
        return 'oneway'
    return 'roundtrip'
