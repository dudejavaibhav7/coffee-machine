import unittest

from coffee_machine.entity.beverage import Beverage


class TestBeverage(unittest.TestCase):
    """Beverage Test Cases
    """

    def test_get_beverage_ingredients(self):
        """Beverage - get beverage ingredients
        """
        beverage_dict = {
            "hot_water": 200,
            "hot_milk": 100,
            "ginger_syrup": 10,
            "sugar_syrup": 10,
            "tea_leaves_syrup": 30
        }
        beverage = Beverage("hot_tea", beverage_dict)
        assert beverage_dict == beverage.get_beverage_ingredients()
