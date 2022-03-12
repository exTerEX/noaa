# NOAA Climate Data Online SDK for Python

Python API for NOAA climate data.

## Getting started

### Prerequisites

To use this interface you need:

- `python 3.7+`

For development you additionaly need:

- `sphinx`

### Installing

#### Intall using pip from source:

Install latest available source using

```
python -m pip install git+https://github.com/exTerEX/noaa.git#egg=noaa
```

Or install specific version (tag, commit, branch) available using

```
python -m pip install git+https://github.com/exTerEX/noaa.git@<branch/commit hash/tag>#egg=noaa
```

where `<branch/commit hash/tag>` is changed out for a specific branch (e.g. main, development), commit hash (e.g. 86ba995, 770f02), or tag (e.g. 0.1.0-alpha, 1.17.6)

#### Install using pip from tarball:

Install latest available source using

```
python -m pip install git+https://github.com/exTerEX/noaa/tarball/main
```

### Usage

Below is a simple example on how to use this API. Get a token from [NOAA](https://www.ncdc.noaa.gov/cdo-web/token) and input it into where `<token>` in the example below.

```python
import noaa

noaaobj = noaa.NOAA("<token>")

print(noaaobj.get_datasets())
print(noaaobj.get_data(
        dataset_id = "GSOM",
        start_date="1970-10-03",
        end_date="2012-09-10")
)
print(noaaobj.get_data_categories())
print(noaaobj.get_data_types())
print(noaaobj.get_locations())
print(noaaobj.get_stations())
```

See [documentation](https://www.ncdc.noaa.gov/cdo-web/webservices/v2) for an in-depth explanation of input values.

### Running tests

TODO: Not implemented yet.

## Contributing

Please read [CONTRIBUTING](https://github.com/exTerEX/noaa/blob/main/.github/CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

This project use [Semantic Versioning](https://semver.org/) for versioning. For the versions available, see the [tags](https://github.com/exTerEX/noaa/tags) on this repository.

## Authors

- _Andreas Sagen_ - Initial contributer

## License

This project is licensed under the `MIT`. For more details see [LICENSE](LICENSE).
