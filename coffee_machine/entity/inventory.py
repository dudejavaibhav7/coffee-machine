from typing import Dict

from coffee_machine.entity.beverage import Beverage
from coffee_machine.entity.ingredient import Ingredient


class Inventory(object):

    def __init__(self, list_of_ingredients: Dict[str, Ingredient]):
        self.list_of_ingredients: Dict[str, Ingredient] = list_of_ingredients

    def get_ingredient(self, ingredient_name):
        if ingredient_name in self.list_of_ingredients:
            return self.list_of_ingredients[ingredient_name]
        else:
            return None

    def create_beverage(self, beverage: Beverage):
        beverage_ingredients: Dict[str, int] = beverage.beverage_ingredients
        for beverage_ingredient in beverage_ingredients:
            if self.get_ingredient(beverage_ingredient) is None:
                raise Exception(f"{beverage_ingredient} is not available")

        for beverage_ingredient in beverage_ingredients:
            ingredient: Ingredient = self.get_ingredient(beverage_ingredient)
            ingredient.check_availability(beverage_ingredients[beverage_ingredient])

        for beverage_ingredient in beverage_ingredients:
            ingredient: Ingredient = self.get_ingredient(beverage_ingredient)
            ingredient.consume(beverage_ingredients[beverage_ingredient])
