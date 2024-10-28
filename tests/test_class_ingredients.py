import pytest
from ingredient import Ingredient
from ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

@pytest.mark.parametrize("ingredient_type, name, price, expected_type, expected_name, expected_price", [
    (INGREDIENT_TYPE_SAUCE, "sauce", 50, INGREDIENT_TYPE_SAUCE, "sauce", 50),
    (INGREDIENT_TYPE_FILLING, "meat", 100, INGREDIENT_TYPE_FILLING, "meat", 100)
])
def test_ingredient_init(ingredient_type, name, price, expected_type, expected_name, expected_price):
    ingredient = Ingredient(ingredient_type, name, price)
    assert ingredient.get_type() == expected_type
    assert ingredient.get_name() == expected_name
    assert ingredient.get_price() == expected_price