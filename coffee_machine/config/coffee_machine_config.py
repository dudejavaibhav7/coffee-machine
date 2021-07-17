class CoffeeMachineConfig(object):
    """
        This is a class for creating a Coffee Machine Config.

        Attributes:
            config (config): The input configuration related to Coffee Machine for initialization of Machine.
            number_of_outlets (int): The Number of Outlets in Machine.
            total_items_quantity (dict): Dictionary Representing input Items Quantity.
            beverages (dict): Dictionary Representing Beverages.
    """
    number_of_outlets = 0
    total_items_quantity = {}
    beverages = {}

    def __init__(self, config):
        """
            The constructor for CoffeeMachineConfig class.
        """
        self.config: dict = config
        self.machine_config: dict = self.config['machine']
        self.number_of_outlets: int = self.machine_config['outlets']['count_n']
        self.total_items_quantity: dict = self.machine_config['total_items_quantity']
        self.beverages: dict = self.machine_config['beverages']


