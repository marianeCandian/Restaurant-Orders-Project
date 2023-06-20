from src.models.ingredient import (
    Ingredient,
    Restriction,
)  # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    ingrediente_1 = Ingredient("queijo mussarela")
    ingrediente_2 = Ingredient("tomate")
    ingrediente_3 = Ingredient("tomate")

    assert ingrediente_1.name == "queijo mussarela"

    assert hash(ingrediente_2) == hash(ingrediente_3)

    assert ingrediente_3 == ingrediente_2
    assert (ingrediente_2 == ingrediente_1) == False

    expected_restrictions = {Restriction.LACTOSE, Restriction.ANIMAL_DERIVED}
    assert ingrediente_1.restrictions == expected_restrictions
