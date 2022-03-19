import unittest
import sys
from noaa.climate import API

if len(sys.argv) != 2:
    sys.exit("ERROR: A command-line parameter must be supplied for these tests")


obj = API(sys.argv[1])


class TestClimateApi(unittest.TestCase):
    def test_get_datasets(self):
        result = obj.get_datasets("GSOM")

        self.assertEqual(result["id"], "GSOM")
        self.assertIsInstance(result, dict)
        self.assertIsNotNone(result)

        result = obj.get_datasets(limit=5)

        result = obj.get_datasets(
            start_date="1970-10-03",
            end_date="2012-09-10"
        )

        self.assertIsInstance(result, dict)
        self.assertIsNotNone(result)

        result = obj.get_datasets(
            start_date="1970-10-03H10:10:10",
            end_date="2012-08-10H10:10:10"
        )

        self.assertIsInstance(result, dict)
        self.assertIsNotNone(result)

        self.assertLessEqual(len(result), 5)
        self.assertIsNotNone(result)

    def test_get_data_categories(self):
        result = obj.get_data_categories("ANNAGR")

        self.assertEqual(result["id"], "ANNAGR")
        self.assertIsInstance(result, dict)
        self.assertIsNotNone(result)

    def test_get_data_types(self):
        result = obj.get_data_types("ACMH")

        self.assertEqual(result["id"], "ACMH")
        self.assertIsInstance(result, dict)
        self.assertIsNotNone(result)

    def test_get_location_categories(self):
        result = obj.get_location_categories("CITY")

    def test_get_locations(self):
        result = obj.get_locations("FIPS:37")

        self.assertEqual(result["id"], "FIPS:37")
        self.assertIsInstance(result, dict)
        self.assertIsNotNone(result)

    def test_get_stations(self):
        result = obj.get_stations("COOP:010957")

        self.assertEqual(result["id"], "COOP:010957")
        self.assertIsInstance(result, dict)
        self.assertIsNotNone(result)

    def test_get_data(self):
        pass


if __name__ == "__main__":
    unittest.main(argv=["first-arg-is-ignored"], exit=False)
