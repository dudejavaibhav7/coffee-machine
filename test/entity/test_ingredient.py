from unittest import TestCase

from coffee_machine.entity.ingredient import Ingredient


class TestIngredient(TestCase):
    """Beverage Test Cases
    """

    def test_check_availability_no_exception(self):
        ingredient = Ingredient("hot_water", 500)
        ingredient.check_availability(200)

    def test_check_availability_exception(self):
        ingredient = Ingredient("hot_water", 0)
        try:
            ingredient.check_availability(200)
        except Exception as e:
            msg = "hot_water is not sufficient \n"
            print(str(e))
            self.assertEqual(str(e), msg)

    def test_consume(self):
        ingredient = Ingredient("hot_water", 500)
        ingredient.consume(200)

        assert ingredient.quantity == 300
