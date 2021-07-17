from typing import Dict

from coffee_machine.config.coffee_machine_config import CoffeeMachineConfig
from coffee_machine.entity.beverage import Beverage
from coffee_machine.entity.beverage_repository import BeverageRepository
from coffee_machine.entity.coffee_machine import CoffeeMachine
from coffee_machine.entity.ingredient import Ingredient
from coffee_machine.entity.inventory import Inventory


class CoffeeMachineFactory(object):

    def __init__(self, coffee_machine_config: CoffeeMachineConfig):
        self.coffee_machine_config = coffee_machine_config

    def create_coffee_machine(self):
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
