import unittest
from tools import getWeather


class TestWeatherIntegration(unittest.TestCase):
    def test_existing_city(self):
        result = getWeather("London")

        self.assertIn("City:", result)
        self.assertIn("Temperature:", result)
        self.assertIn("Condition:", result)
        self.assertIn("Humidity:", result)
        self.assertIn("Wind speed:", result)

    def test_not_existing_city(self):
        fake_city = "asldkjasldkjasldkjaslkdj"
        with self.assertRaises(ValueError):
            getWeather(fake_city)


if __name__ == "__main__":
    unittest.main()
