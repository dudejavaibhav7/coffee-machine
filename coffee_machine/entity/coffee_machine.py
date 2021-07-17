from coffee_machine.entity.beverage_repository import BeverageRepository
from coffee_machine.entity.inventory import Inventory


class CoffeeMachine(object):

    def __init__(self, num_of_outlets: int, beverage_repository: BeverageRepository, inventory: Inventory):
        self.num_of_outlets = num_of_outlets
        self.beverage_repository = beverage_repository
        self.inventory = inventory

    def request_beverage(self, beverage_name: str):
        if self.beverage_repository.get_beverage(beverage_name) is None:
            raise Exception(f"Beverage name: {beverage_name} is not present in Beverage Repository")
        else:
            beverage = self.beverage_repository.get_beverage(beverage_name)
            try:
                self.inventory.create_beverage(beverage)
                print(f"{beverage_name} is prepared")
            except Exception as e:
                print(f"{beverage_name} cannot be prepared because {e}")

