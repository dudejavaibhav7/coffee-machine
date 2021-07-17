from unittest import TestCase

from coffee_machine.run_coffee_machine import run_coffee_machine


class TestRunCoffeeMachine(TestCase):

    def test_run_coffee_machine(self):
        file_path = "resources/test_input_1.json"
        beverage_list = "hot_tea,black_tea,hot_coffee,green_tea,hot_tea,black_tea"
        run_coffee_machine(file_path, beverage_list)



