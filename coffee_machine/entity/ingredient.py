class Ingredient(object):
    """
        This is a class of an Ingredient.

        Attributes:
            name (str): Name of the Ingredient.
            quantity(int): Quantity of the Ingredient.
    """

    def __init__(self, name, quantity):
        """
            The constructor for Ingredient class.

            Parameters:
                name (str): Name of the Ingredient.
                quantity(int): Quantity of the Ingredient.
        """
        self.name: str = name
        self.quantity: int = quantity

    def check_availability(self, quantity_required: int):
        """
            The function to check availability of Ingredient.

            Parameters:
               quantity_required (int): The quantity required for Ingredient.
            Returns:
                Exception in case of any problem
        """
        if self.quantity == 0:
            raise Exception(f"{self.name} is not sufficient \n")
        elif self.quantity < quantity_required:
            raise Exception(f"{self.name} is not sufficient \n")

    def consume(self, quantity_required: int):
        """
            The function to consume the Ingredient.

            Parameters:
               quantity_required (int): The quantity required for Ingredient.
            Returns:
                Exception in case of any problem otherwise subtract the quantity used.
        """
        self.check_availability(quantity_required)
        self.quantity -= quantity_required
