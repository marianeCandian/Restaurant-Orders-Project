from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient
import pytest


# Req 2
def test_dish():
    dish = Dish("Fejoada", 20.0)
    assert dish.name == "Fejoada"

    dish1 = Dish("Fejoada", 20.0)
    dish2 = Dish("Fejoada", 20.0)
    assert hash(dish1) == hash(dish2)
    assert dish1 == dish2

    dish1 = Dish("Fejoada", 20.0)
    dish3 = Dish("Macarronada", 10.9)
    assert hash(dish1) != hash(dish3)
    assert dish1 != dish3

    assert repr(dish) == "Dish('Fejoada', R$20.00)"

    with pytest.raises(TypeError):
        Dish("Fejoada", "invalid")
    with pytest.raises(ValueError):
        Dish("Fejoada", -20.0)

    ingredient = Ingredient("Macarrão")
    dish = Dish("Macarronada", 10.9)
    dish.add_ingredient_dependency(ingredient, 2)
    assert dish.recipe.get(ingredient) == 2

    ingredient1 = Ingredient("Macarrão")
    ingredient2 = Ingredient("Molho")
    dish = Dish("Macarronada", 10.9)
    dish.add_ingredient_dependency(ingredient1, 2)
    dish.add_ingredient_dependency(ingredient2, 1)
    assert dish.get_restrictions() == set()

    dish = Dish("Macarronada", 10.9)
    dish.add_ingredient_dependency(ingredient1, 2)
    dish.add_ingredient_dependency(ingredient2, 1)
    assert dish.get_ingredients() == {ingredient1, ingredient2}
