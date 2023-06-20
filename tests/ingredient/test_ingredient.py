from src.models.ingredient import (
    Ingredient,
    Restriction,
)  # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    ingredient = Ingredient("Frango")
    assert ingredient.name == "Frango"
    assert ingredient.restrictions == set()

    assert repr(ingredient) == "Ingredient('Frango')"

    ingredient1 = Ingredient("Frango")
    ingredient2 = Ingredient("Frango")
    assert ingredient1 == ingredient2

    assert hash(ingredient1) == hash(ingredient2)

    ingredient3 = Ingredient("cebola")
    assert ingredient1 != ingredient3
    assert hash(ingredient1) != hash(ingredient3)

    ingredient = Ingredient("queijo mussarela")
    expected_restrictions = {Restriction.LACTOSE, Restriction.ANIMAL_DERIVED}
    assert ingredient.restrictions == expected_restrictions
