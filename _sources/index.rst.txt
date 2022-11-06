Welcome to NOAA's documentation!
================================

.. toctree::
   :hidden:
   :maxdepth: 2

   documentation
   examples

NOAA is a Python API to the Climate Data Online (CDO) database from the
National Oceanic and Atmospheric Administration. The API provide access to
NCDC's archive of global historical weather and climate data in addition to
station history information.

**Note:** The API is currently in development, and could break at any time.

Getting started
--------------------------------

To use the API you require:

* Python 3.7+

Install the python module using pip:

.. code-block:: shell

   python -m pip install git+https://github.com/exTerEX/noaa.git#egg=noaa

To use the API you will also have to get an access token from NOAA. Get it
from NOAA's website `here`_.

.. _here: https://www.ncdc.noaa.gov/cdo-web/token

Example
--------------------------------

TODO: Add a simple examples

For more examples and/or more advanced use cases, see :doc:`examples`.
