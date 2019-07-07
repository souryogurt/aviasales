# -*- coding: utf-8 -*-
"""Web service that provides flights API"""

import argparse
import sys
from aiohttp import web
from . import partner

__all__ = ['main']


async def get_tickets(request):
    """Handle /tickets request and return tickets list as JSON."""
    tickets_type = request.query.get('type', 'oneway').lower()
    if tickets_type not in ['oneway', 'roundtrip']:
        raise web.HTTPBadRequest()
    tickets = await partner.fetch_tickets(tickets_type)
    return web.json_response(tickets)


def main():
    """Entry point."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--verbose', action='store_true', help='be verbose')
    parser.add_argument('-H', '--host', help='host address to listen on')
    parser.add_argument('-p', '--path', help='unix socket path to listen on')
    parser.add_argument('-P', '--port', help='TCP port to listen on')
    args = parser.parse_args()
    app = web.Application()
    app.router.add_get('/tickets', get_tickets)
    web.run_app(app, host=args.host, port=args.port, path=args.path)


if __name__ == "__main__":
    sys.exit(main())
