# -*- coding: utf-8 -*-
"""Web service that provides flights API"""

import argparse
import sys
from aiohttp import web
from . import partner

__all__ = ['main']


async def get_itineraries(request):
    """Handle /itineraries request and return itineraries list as JSON."""
    itineraries_type = request.query.get('type', 'oneway').lower()
    if itineraries_type not in ['oneway', 'roundtrip']:
        raise web.HTTPBadRequest()
    itineraries = await partner.fetch_itineraries(itineraries_type)
    return web.json_response(itineraries)


def main():
    """Entry point."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('-H', '--host', help='host address to listen on')
    parser.add_argument('-p', '--path', help='unix socket path to listen on')
    parser.add_argument('-P', '--port', help='TCP port to listen on')
    args = parser.parse_args()
    app = web.Application()
    app.router.add_get('/itineraries', get_itineraries)
    web.run_app(app, host=args.host, port=args.port, path=args.path)


if __name__ == "__main__":
    sys.exit(main())
