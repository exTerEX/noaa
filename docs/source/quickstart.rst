Quickstart Guide
================

This guide will help you get started with the NOAA Climate API client.

Installation
------------

Install the package using pip::

    pip install noaa-climate

Or using uv::

    uv pip install noaa-climate

Getting Your API Token
-----------------------

1. Go to https://www.ncdc.noaa.gov/cdo-web/token
2. Enter your email address
3. Check your email for the token (usually arrives within minutes)
4. Save your token securely

Basic Usage
-----------

Initialize the Client
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    from noaa import NOAA

    client = NOAA("your-api-token-here")

Explore Available Datasets
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    # Get all datasets
    datasets = client.get_datasets()
    
    for dataset in datasets['results']:
        print(f"{dataset['id']}: {dataset['name']}")

Get Information About a Specific Dataset
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    # Get details for GHCND (Daily Summaries)
    ghcnd = client.get_datasets(dataset_id="GHCND")
    print(ghcnd)

Find Stations
~~~~~~~~~~~~~

.. code-block:: python

    # Find stations in a specific location
    stations = client.get_stations(
        dataset_id="GHCND",
        location_id="FIPS:37",  # North Carolina
        limit=10
    )
    
    for station in stations['results']:
        print(f"{station['name']}: {station['id']}")

Retrieve Climate Data
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    # Get temperature data for a station
    data = client.get_data(
        dataset_id="GHCND",
        station_id="GHCND:USW00094728",  # Central Park, NY
        start_date="2023-01-01",
        end_date="2023-01-31",
        data_type_id=["TMAX", "TMIN"],  # Max and min temperature
        units="metric"
    )
    
    for record in data['results']:
        print(f"{record['date']}: {record['datatype']} = {record['value']}°C")

Working with Multiple IDs
~~~~~~~~~~~~~~~~~~~~~~~~~~

You can pass lists for ID parameters to filter by multiple values:

.. code-block:: python

    # Get data from multiple stations
    data = client.get_data(
        dataset_id="GHCND",
        station_id=[
            "GHCND:USW00094728",  # Central Park, NY
            "GHCND:USW00013722"   # Miami, FL
        ],
        start_date="2023-01-01",
        end_date="2023-01-31",
        data_type_id="TMAX"
    )

Pagination
~~~~~~~~~~

For large result sets, use limit and offset:

.. code-block:: python

    # Get first 1000 results
    page1 = client.get_stations(dataset_id="GHCND", limit=1000, offset=0)
    
    # Get next 1000 results
    page2 = client.get_stations(dataset_id="GHCND", limit=1000, offset=1000)

Error Handling
--------------

The library raises ``ValidationError`` for invalid inputs:

.. code-block:: python

    from noaa import NOAA
    from noaa.exceptions import ValidationError

    client = NOAA("your-token")

    try:
        # This will raise ValidationError (limit too high)
        data = client.get_datasets(limit=2000)
    except ValidationError as e:
        print(f"Invalid input: {e}")

Next Steps
----------

* Check out the :doc:`examples` for more detailed use cases
* Read the :doc:`api` for complete API reference