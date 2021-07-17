class Ingredient(object):

    def __init__(self, name, quantity):
        self.name: str = name
        self.quantity: int = quantity

    def check_availability(self, quantity_required: int):
        if self.quantity == 0:
            raise Exception(f"{self.name} is not sufficient")
        elif self.quantity < quantity_required:
            raise Exception(f"{self.name} is not sufficient")

    def consume(self, quantity_required: int):
        self.check_availability(quantity_required)
        self.quantity -= quantity_required
