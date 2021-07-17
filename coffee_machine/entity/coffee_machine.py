from coffee_machine.entity.beverage_repository import BeverageRepository
from coffee_machine.entity.inventory import Inventory


class CoffeeMachine(object):
    """
        This is a class of Coffee Machine.

        Attributes:
            num_of_outlets (int): The Number of Outlets in Machine.
            beverage_repository (BeverageRepository): Repository for Beverage.
            inventory (Inventory): Inventory for stock.
    """

    def __init__(self, num_of_outlets: int, beverage_repository: BeverageRepository, inventory: Inventory):
        """
            The constructor for CoffeeMachine class.
            Parameters:
                num_of_outlets (int): The Number of Outlets in Machine.
                beverage_repository (BeverageRepository): Repository for Beverage.
                inventory (Inventory): Inventory for stock.
        """
        self.num_of_outlets = num_of_outlets
        self.beverage_repository = beverage_repository
        self.inventory = inventory

    def request_beverage(self, beverage_name: str):
        """
            The function to get a Beverage.
            Parameters:
               beverage_name (str): The Name of Beverage.
            Returns:
                Confirmation on creating a Beverage or Exception in case of any problem.
        """
        if self.beverage_repository.get_beverage(beverage_name) is None:
            raise Exception(f"Beverage name: {beverage_name} is not present in Beverage Repository \n")
        else:
            beverage = self.beverage_repository.get_beverage(beverage_name)
            try:
                self.inventory.create_beverage(beverage)
                print(f"{beverage_name} is prepared \n")
            except Exception as e:
                print(f"{beverage_name} cannot be prepared because {e}")

