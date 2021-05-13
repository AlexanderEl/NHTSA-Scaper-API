import unittest
import sys
sys.path.append('..')
import processing


class TestMakes(unittest.TestCase):

    def test_manufacturing(self):
        manufacturers = processing.get_list_of_manufacturers()
        self.assertTrue(manufacturers)

    def test_valid_manufacturer(self):
        makes = processing.get_all_makes_for_manufacturer("Toyota")
        self.assertTrue(makes)

    def test_invalid_manufacturer(self):
        makes = processing.get_all_makes_for_manufacturer(987654321)
        self.assertTrue(makes)
        makes = processing.get_all_makes_for_manufacturer(None)
        self.assertTrue(makes)

    def test_valid_vin(self):
        data = processing.get_vehicle_info_from_vin("3n1ab6ap7bl729215")
        self.assertTrue(data)
        data = processing.get_vehicle_info_from_vin("4A4AR3AU3FE030613")
        self.assertTrue(data)
        data = processing.get_vehicle_info_from_vin("5LMEU27R92LJ44473")
        self.assertTrue(data)

    def test_invalid_vin(self):
        data = processing.get_vehicle_info_from_vin("5")
        self.assertTrue(data)
        data = processing.get_vehicle_info_from_vin("qwerty")
        self.assertTrue(data)
        data = processing.get_vehicle_info_from_vin(5)
        self.assertTrue(data)
        data = processing.get_vehicle_info_from_vin(None)
        self.assertTrue(data)


if __name__ == '__main__':
    unittest.main()
