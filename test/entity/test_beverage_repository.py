from typing import Dict
from unittest import TestCase

from coffee_machine.entity.beverage import Beverage
from coffee_machine.entity.beverage_repository import BeverageRepository


class TestBeverageRepository(TestCase):
    """Beverage Repository Test Cases
    """

    def test_get_beverage_present(self):
        """Beverage - get beverage - present
        """
        beverages = {
            "hot_tea": {
                "hot_water": 200,
                "hot_milk": 100,
                "ginger_syrup": 10,
                "sugar_syrup": 10,
                "tea_leaves_syrup": 30
            },
            "hot_coffee": {
                "hot_water": 100,
                "ginger_syrup": 30,
                "hot_milk": 400,
                "sugar_syrup": 50,
                "tea_leaves_syrup": 30
            },
            "black_tea": {
                "hot_water": 300,
                "ginger_syrup": 30,
                "sugar_syrup": 50,
                "tea_leaves_syrup": 30
            },
            "green_tea": {
                "hot_water": 100,
                "ginger_syrup": 30,
                "sugar_syrup": 50,
                "green_mixture": 30
            }
        }
        all_beverages: Dict[str, Beverage] = {}
        for key in beverages:
            beverage = Beverage(key, beverages[key])
            all_beverages[key] = beverage

        beverage = Beverage("black_tea", {
            "hot_water": 300,
            "ginger_syrup": 30,
            "sugar_syrup": 50,
            "tea_leaves_syrup": 30
        })

        beverage_repository = BeverageRepository(all_beverages)
        assert beverage.beverage_ingredients == beverage_repository.get_beverage("black_tea").get_beverage_ingredients()
        assert beverage.name == beverage_repository.get_beverage("black_tea").name

    def test_get_beverage_not_present(self):
        """Beverage - get beverage - not present
        """
        beverages = {
            "hot_tea": {
                "hot_water": 200,
                "hot_milk": 100,
                "ginger_syrup": 10,
                "sugar_syrup": 10,
                "tea_leaves_syrup": 30
            },
            "hot_coffee": {
                "hot_water": 100,
                "ginger_syrup": 30,
                "hot_milk": 400,
                "sugar_syrup": 50,
                "tea_leaves_syrup": 30
            },
            "black_tea": {
                "hot_water": 300,
                "ginger_syrup": 30,
                "sugar_syrup": 50,
                "tea_leaves_syrup": 30
            },
            "green_tea": {
                "hot_water": 100,
                "ginger_syrup": 30,
                "sugar_syrup": 50,
                "green_mixture": 30
            }
        }
        all_beverages: Dict[str, Beverage] = {}
        for key in beverages:
            beverage = Beverage(key, beverages[key])
            all_beverages[key] = beverage

        beverage_repository = BeverageRepository(all_beverages)
        assert beverage_repository.get_beverage("random_tea") is None
