# -*- coding: utf-8 -*-
"""Web service that provides flights API"""

import argparse
import sys
from aiohttp import web


__all__ = ['main']


async def index(request):
    """Handle request and return response."""
    return web.Response(text='Hello there!')


def main():
    """Entry point."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--verbose', action='store_true', help='be verbose')
    parser.add_argument('-i', '--host', help='host address to listen on')
    parser.add_argument('-u', '--path', help='unix socket path to listen on')
    parser.add_argument('-p', '--port', help='TCP port to listen on')
    args = parser.parse_args()
    app = web.Application()
    app.router.add_get('/', index)
    web.run_app(app, host=args.host, port=args.port, path=args.path)


if __name__ == "__main__":
    sys.exit(main())
