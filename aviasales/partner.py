# -*- coding: utf-8 -*-
"""Module that provides API to partner service"""

from xml.etree import ElementTree as ET
from typing import List
from pkg_resources import resource_filename
from .models import Itinerary, ItineraryType

RESPONSE_MOCKS = {
    ItineraryType.ONEWAY: resource_filename('aviasales', 'RS_ViaOW.xml'),
    ItineraryType.ROUNDTRIP: resource_filename('aviasales', 'RS_Via-3.xml')
}

__all__ = ['fetch_itineraries']


async def fetch_itineraries(itinerary_type: ItineraryType) -> List[Itinerary]:
    """Make call to partner API and return list of tickets."""
    # In case of actual service, here we can make real HTTP request, but right
    # now we are just using predefined response.
    xml = ET.parse(RESPONSE_MOCKS[ItineraryType(itinerary_type)])
    tickets = list()
    for priced_flight in xml.findall('.//PricedItineraries/Flights'):
        tickets.append(Itinerary())
    return tickets


def get_ticket_type(ticket):
    """Parse ticket and return ticket type either 'oneway' or 'roundtrip'."""
    if not ticket.find('.//ReturnPricedItinerary'):
        return 'oneway'
    return 'roundtrip'
