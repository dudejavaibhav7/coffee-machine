from typing import Dict

from coffee_machine.config.coffee_machine_config import CoffeeMachineConfig
from coffee_machine.entity.beverage import Beverage
from coffee_machine.entity.beverage_repository import BeverageRepository
from coffee_machine.entity.coffee_machine import CoffeeMachine
from coffee_machine.entity.ingredient import Ingredient
from coffee_machine.entity.inventory import Inventory


class CoffeeMachineFactory(object):
    """
        This is a class for creating a Coffee Machine.

        Attributes:
            coffee_machine_config (CoffeeMachineConfig): The configuration related to Coffee Machine.
    """

    def __init__(self, coffee_machine_config: CoffeeMachineConfig):
        """
            The constructor for CoffeeMachineFactory class.

            Parameters:
               coffee_machine_config (CoffeeMachineConfig): The configuration related to Coffee Machine.
        """
        self.coffee_machine_config = coffee_machine_config

    def create_coffee_machine(self):
        """
            The function to create Coffee Machine.

            Returns:
                CoffeeMachine: A Coffee Machine Object containing Inventory, Beverage Repository and Num of Outlets.
        """
        num_of_outlets: int = self.coffee_machine_config.number_of_outlets
        total_items_quantity: dict = self.coffee_machine_config.total_items_quantity
        beverages: dict = self.coffee_machine_config.beverages

        all_ingredients: Dict[str, Ingredient] = {}
        for key in total_items_quantity:
            ingredient = Ingredient(key, total_items_quantity[key])
            all_ingredients[key] = ingredient

        all_beverages: Dict[str, Beverage] = {}
        for key in beverages:
            beverage = Beverage(key, beverages[key])
            all_beverages[key] = beverage

        beverage_repository = BeverageRepository(all_beverages)
        inventory = Inventory(all_ingredients)

        coffee_machine = CoffeeMachine(num_of_outlets, beverage_repository, inventory)

        return coffee_machine
