# -*- coding: utf-8 -*-
"""Web service that provides flights API"""

import argparse
import sys


__all__ = ['main']


def main():
    """Entry point."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--verbose', action='store_true', help='be verbose')
    args = parser.parse_args()


if __name__ == "__main__":
    sys.exit(main())
