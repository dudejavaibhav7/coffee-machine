from typing import Dict

from coffee_machine.entity.beverage import Beverage


class BeverageRepository(object):

    def __init__(self, list_of_beverages: Dict[str, Beverage]):
        self.list_of_beverages: Dict[str, Beverage] = list_of_beverages

    def get_beverage(self, name):
        if name in self.list_of_beverages:
            return self.list_of_beverages[name]
        else:
            return None
