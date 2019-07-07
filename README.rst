aviasales
=========

Solution for the tasks of assessted team. The web service that provides the
following API:

Installation
------------

Install aviasales from git repository, by running::

    git clone https://github.com/souryogurt/aviasales.git
    cd aviasales
    python3 -m venv .venv
    source .venv/bin/activate
    pip install -e .

Usage
-----

Run service just by invoking ``aviasales`` command. Service also accepts flags::

    usage: aviasales [-h] [--verbose] [-H HOST] [-p PATH] [-P PORT]

    Web service that provides flights API

    optional arguments:
      -h, --help            show this help message and exit
      --verbose             be verbose
      -H HOST, --host HOST  host address to listen on
      -p PATH, --path PATH  unix socket path to listen on
      -P PORT, --port PORT  TCP port to listen on

Contribute
----------
- Issue Tracker: https://github.com/souryogurt/aviasales/issues
- Source Code: https://github.com/souryogurt/aviasales

Support
-------

If you are having issues, please let me know.
* Egor Artemov <egor.artemov@gmail.com>
