from typing import Dict


class Beverage:
    """
        This is a class of a Beverage.

        Attributes:
            beverage_ingredients (Dict): The Dictionary containing Beverage Ingredients.
    """

    def __init__(self, name: str, beverage_ingredients: Dict[str, int]):
        """
            The constructor for Beverage class.

            Parameters:
               beverage_ingredients (Dict): The Dictionary containing Beverage Ingredients.
               name (str): Name of Beverage.
        """
        self.name: str = name
        self.beverage_ingredients: Dict[str, int] = beverage_ingredients

    def get_beverage_ingredients(self):
        """
            The function to get Beverage Ingredients.

            Returns: beverage_ingredients Dict
        """
        return self.beverage_ingredients
