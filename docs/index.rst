NOAA Climate Data Online API Documentation
===========================================

Welcome to the NOAA Climate Data Online (CDO) API Python client documentation.
This library provides a convenient interface to access historical weather and
climate data from NOAA's extensive archive.

.. toctree::
   :hidden:
   :maxdepth: 2
   :caption: Contents:

   quickstart
   api
   examples

Features
--------

* Simple, intuitive interface to NOAA CDO API
* Full coverage of all CDO endpoints
* Comprehensive input validation
* Type hints for better IDE support
* Extensive test coverage
* Well-documented with examples

Installation
------------

Using pip:

.. code-block:: shell

    pip install noaa-climate

Using uv:

.. code-block:: shell

    uv pip install noaa-climate

Quick Example
-------------

.. code-block:: python

    from noaa import NOAA

    # Initialize client with your API token
    client = NOAA("your-api-token-here")

    # Get available datasets
    datasets = client.get_datasets(limit=10)

    # Get temperature data for a location
    data = client.get_data(
        dataset_id="GHCND",
        station_id="GHCND:USW00094728",
        start_date="2023-01-01",
        end_date="2023-01-31",
        data_type_id=["TMAX", "TMIN"]
    )

Getting an API Token
--------------------

To use this library, you need an API token from NOAA:

1. Visit https://www.ncdc.noaa.gov/cdo-web/token
2. Enter your email address
3. You'll receive a token via email (usually within minutes)

API Overview
------------

The client provides access to these main endpoints:

**Datasets**
    Access available climate datasets (GHCND, GSOM, etc.)

**Data Categories**
    Browse data categories (Temperature, Precipitation, etc.)

**Data Types**
    Explore specific data types (TMAX, TMIN, PRCP, etc.)

**Locations**
    Search and filter geographic locations

**Stations**
    Find weather stations and their metadata

**Data**
    Retrieve actual climate observations

Indices and Tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`