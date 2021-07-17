import argparse
import json
import random
import threading
from typing import List

from coffee_machine.config.coffee_machine_config import CoffeeMachineConfig
from coffee_machine.entity.coffee_machine import CoffeeMachine
from coffee_machine.factory.coffee_machine_factory import CoffeeMachineFactory


def divide_chunks(lis: list, n: int):
    """
        The function to get Ingredient.

        Parameters:
           lis (List): The List.
           n (int): size of chunk
        Returns:
            List of List of chunks of size n.
    """
    # looping till length l
    for x in range(0, len(lis), n):
        yield lis[x:x + n]


def run_coffee_machine(file_path: str, beverage_list: str):
    # Opening File to extract input data
    with open(file_path) as f:
        input_data = json.load(f)
        # Closing File
        f.close()

    # Creating Coffee Machine Config
    coffee_machine_config = CoffeeMachineConfig(input_data)
    num_of_outlets: int = coffee_machine_config.number_of_outlets

    # Creating Instance of Coffee Machine
    coffee_machine: CoffeeMachine = CoffeeMachineFactory(coffee_machine_config).create_coffee_machine()

    # Creating Input Beverage List from user Input
    input_beverage_list: List[str] = [beverage.strip() for beverage in beverage_list.split(',')]
    input_beverage_size = len(input_beverage_list)

    # Case if size is less than num of outlets
    if num_of_outlets >= input_beverage_size:
        threads = list()
        random.shuffle(input_beverage_list)
        for beverage_name in input_beverage_list:
            # We start one thread per beverage present.
            process = threading.Thread(target=coffee_machine.request_beverage, args=(beverage_name,))
            process.start()

        # We now pause execution on the main thread by 'joining' all of our started threads.
        # This ensures that each has finished processing the urls.
        for process in threads:
            process.join()

    # Case if size is greater than num of outlets
    else:
        n_input_beverage_list = divide_chunks(input_beverage_list, num_of_outlets)
        i = 1
        # Running Machine for n inputs until we consume all inputs
        for input_beverage_list in n_input_beverage_list:
            print("-----------------------------------")
            print(f"Starting Coffee Machine for {i}th iteration of n beverages")
            random.shuffle(input_beverage_list)

            threads = list()
            for beverage_name in input_beverage_list:
                # We start one thread per beverage present.
                process = threading.Thread(target=coffee_machine.request_beverage, args=(beverage_name,))
                process.start()

            # We now pause execution on the main thread by 'joining' all of our started threads.
            # This ensures that each has finished processing the urls.
            for process in threads:
                process.join()
            print("-----------------------------------")
            i += 1


if __name__ == '__main__':
    parser: argparse.ArgumentParser = argparse.ArgumentParser()
    # File Path Argument
    parser.add_argument('file_path', type=str, help='Input File Path')
    parser.add_argument('beverage_list', type=str, help='Input beverage List separated by comma')
    arguments = parser.parse_args()

    run_coffee_machine(arguments.file_path, arguments.beverage_list)
