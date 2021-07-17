class CoffeeMachineConfig(object):
    number_of_outlets = 0
    total_items_quantity = {}
    beverages = {}

    def __init__(self, config):
        self.config: dict = config
        self.machine_config: dict = self.config['machine']
        self.number_of_outlets: int = self.machine_config['outlets']['count_n']
        self.total_items_quantity: dict = self.machine_config['total_items_quantity']
        self.beverages: dict = self.machine_config['beverages']


