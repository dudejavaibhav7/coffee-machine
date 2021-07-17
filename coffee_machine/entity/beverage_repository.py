from typing import Dict

from coffee_machine.entity.beverage import Beverage


class BeverageRepository(object):
    """
        This is a class for creating a Beverage Repository.

        Attributes:
            list_of_beverages (Dict): The Dictionary containing Beverages.
    """

    def __init__(self, list_of_beverages: Dict[str, Beverage]):
        """
            The constructor for Beverage Repository class.

            Parameters:
               list_of_beverages (Dict): The Dictionary containing Beverages.
        """
        self.list_of_beverages: Dict[str, Beverage] = list_of_beverages

    def get_beverage(self, name):
        """
            The function to get Beverage.

            Parameters:
               name (str): Name of Beverage.

            Returns: beverage if present otherwise None.
        """
        if name in self.list_of_beverages:
            return self.list_of_beverages[name]
        else:
            return None
