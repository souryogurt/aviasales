# -*- coding: utf-8 -*-
"""Module that provides API to partner service"""

import asyncio
import sys
import argparse
from xml.etree import ElementTree as ET
from pkg_resources import resource_filename

__all__ = ['fetch_itineraries']

RESPONSE_MOCKS = {
    'oneway': resource_filename('aviasales', 'RS_ViaOW.xml'),
    'roundtrip': resource_filename('aviasales', 'RS_Via-3.xml')
}


async def fetch_itineraries(itineraries_type):
    """Make call to partner API and return list of itineraries."""
    # In case of actual service, here we can make real HTTP request, but right
    # now we are just using predefined response.
    xml = ET.parse(RESPONSE_MOCKS[itineraries_type])
    itineraries = list()
    for itinerary in xml.findall('.//PricedItineraries/Flights'):
        itineraries.append({
            'onward': parse_flights(itinerary.findall('.//OnwardPricedItinerary/Flights/Flight')),
            'return': parse_flights(itinerary.findall('.//ReturnPricedItinerary/Flights/Flight')),
            'pricing': parse_pricing(itinerary.find('.//Pricing')),
        })
    return itineraries


def parse_flights(flights):
    """Parse xml tree and return flights list."""
    if not flights:
        return None
    result = list()
    for flight in flights:
        result.append({
            'carrier': flight.findtext('./Carrier').strip(),
            'flight_number': flight.findtext('./FlightNumber').strip(),
            'departure_ts': flight.findtext('./DepartureTimeStamp').strip(),
            'arrival_ts': flight.findtext('./ArrivalTimeStamp').strip(),
            'class': flight.findtext('./Class').strip(),
            'fare_basis': flight.findtext('./FareBasis').strip(),
            'ticket_type': flight.findtext('./TicketType').strip(),
        })
    return result


def parse_pricing(pricing):
    """Parse xml tree and return pricing list."""
    price = {
        'currency': pricing.get('currency').strip(),
    }
    return price


async def print_itineraries(itineraries_type):
    """Fetch and print itineraries."""
    itineraries = await fetch_itineraries(itineraries_type)
    for itenerary in itineraries:
        print(itenerary)


def main():
    """Partner API debug commandline entrypoint."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('type', choices=['oneway', 'roundtrip'])
    args = parser.parse_args()
    asyncio.get_event_loop().run_until_complete(print_itineraries(args.type))


if __name__ == "__main__":
    sys.exit(main())
