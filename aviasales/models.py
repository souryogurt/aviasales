# -*- coding: utf-8 -*-
"""Module that provides core aviasales models"""

from dataclasses import dataclass, field
from typing import List
from enum import Enum
from decimal import Decimal
from datetime import datetime


class ItineraryType(Enum):
    """Itinerary type"""
    ONEWAY = "oneway"
    ROUNDTRIP = "roundtrip"


@dataclass
class Carrier:
    """Carrier name"""
    id: str
    name: str


@dataclass
class Flight:
    """Flight in particular itinerary"""
    carrier: Carrier
    number: int
    source: str
    destination: str
    departure: datetime
    arrival: datetime
    flightclass: str
    stops: int
    farebasis: str
    ticket_type: str


class PriceCategory(Enum):
    """Service charge type"""
    SINGLE_ADULT = "SingleAdult"
    SINGLE_CHILD = "SingleChild"
    SINGLE_INFANT = "SingleInfant"


class ChargeType(Enum):
    """Service charge type"""
    BASE_FARE = "BaseFare"
    AIRLINE_TAXES = "AirlineTaxes"


@dataclass
class Charge:
    """Itinerary charges"""
    type: ChargeType
    amount: Decimal


@dataclass
class Price:
    """Pricing for service charge"""
    currency: str
    category: PriceCategory
    total: Decimal
    charges: List[Charge] = field(default_factory=list)


@dataclass
class Itinerary:
    """Complex itinerary from one cyty to another"""
    onward_flights: List[Flight] = field(default_factory=list)
    return_flights: List[Flight] = field(default_factory=list)
    pricing: List[Price] = field(default_factory=list)
