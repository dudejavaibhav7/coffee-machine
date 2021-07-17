from typing import Dict


class Beverage(object):

    def __init__(self, name, beverage_ingredients):
        self.name: str = name
        self.beverage_ingredients: Dict[str, int] = beverage_ingredients

    def get_beverage_ingredients(self):
        return self.beverage_ingredients
