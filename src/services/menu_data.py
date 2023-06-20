import csv
from typing import List
from models.dish import Dish
from models.ingredient import Ingredient


class MenuData:
    def __init__(self, source_path: str) -> None:
        self.source_path = source_path
        self.dishes = set()
        self._load_menu_data()

    def _load_menu_data(self) -> None:
        with open(self.source_path, "r", newline="") as csvfile:
            reader = csv.reader(csvfile)
            next(reader)  # Skip header row
            dish_ingredients = {}
            for row in reader:
                dish_name = row[0]
                price = float(row[1])
                ingredient_name = row[2]
                quantity = int(row[3])
                ingredient = Ingredient(ingredient_name)
                if dish_name not in dish_ingredients:
                    dish = Dish(dish_name, price)
                    self.dishes.add(dish)
                    dish_ingredients[dish_name] = []
                dish_ingredients[dish_name].append((ingredient, quantity))

            for dish_name, ingredients in dish_ingredients.items():
                dish = next(
                    (dish for dish in self.dishes if dish.name == dish_name),
                    None,
                )
                if dish:
                    for ingredient, quantity in ingredients:
                        dish.add_ingredient_dependency(ingredient, quantity)
