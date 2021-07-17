import argparse
import json

from coffee_machine.config.coffee_machine_config import CoffeeMachineConfig
from coffee_machine.entity.coffee_machine import CoffeeMachine
from coffee_machine.factory.coffee_machine_factory import CoffeeMachineFactory

if __name__ == '__main__':
    parser: argparse.ArgumentParser = argparse.ArgumentParser()
    parser.add_argument('file_path', type=str, help='Input File Path')
    args = parser.parse_args()

    with open(args.file_path) as f:
        input_data = json.load(f)
        f.close()

    coffee_machine_config = CoffeeMachineConfig(input_data)
    coffee_machine: CoffeeMachine = CoffeeMachineFactory(coffee_machine_config).create_coffee_machine()

    coffee_machine.request_beverage("hot_tea")
    coffee_machine.request_beverage("black_tea")
    coffee_machine.request_beverage("green_tea")
    coffee_machine.request_beverage("hot_coffee")
