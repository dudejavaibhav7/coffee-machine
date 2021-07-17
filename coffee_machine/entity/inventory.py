from typing import Dict

from coffee_machine.entity.beverage import Beverage
from coffee_machine.entity.ingredient import Ingredient


class Inventory(object):
    """
        This is a class of an Inventory.

        Attributes:
            list_of_ingredients (dict): List of Ingredients.
    """

    def __init__(self, list_of_ingredients: Dict[str, Ingredient]):
        """
            The constructor for Inventory class.

            Parameters:
                list_of_ingredients (dict): List of Ingredients.
        """
        self.list_of_ingredients: Dict[str, Ingredient] = list_of_ingredients

    def get_ingredient(self, ingredient_name: str):
        """
            The function to get Ingredient.

            Parameters:
               ingredient_name (str): The name of Ingredient.
            Returns:
                Ingredient in case it is present else None.
        """
        if ingredient_name in self.list_of_ingredients:
            return self.list_of_ingredients[ingredient_name]
        else:
            return None

    def create_beverage(self, beverage: Beverage):
        """
            The function to create a Beverage.

            Parameters:
               beverage (Beverage): Beverage Object that needs to be created.
            Returns:
                Exception in case of any problem else Confirmation of Creation.
        """
        beverage_ingredients: Dict[str, int] = beverage.get_beverage_ingredients()
        for beverage_ingredient in beverage_ingredients:
            if self.get_ingredient(beverage_ingredient) is None:
                raise Exception(f"{beverage_ingredient} is not available \n")

        for beverage_ingredient in beverage_ingredients:
            ingredient: Ingredient = self.get_ingredient(beverage_ingredient)
            ingredient.check_availability(beverage_ingredients[beverage_ingredient])

        for beverage_ingredient in beverage_ingredients:
            ingredient: Ingredient = self.get_ingredient(beverage_ingredient)
            ingredient.consume(beverage_ingredients[beverage_ingredient])
