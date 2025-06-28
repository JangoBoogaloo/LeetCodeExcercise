from typing import List


class Solution:
    def _canCreate(self, item: str, ingredientsOf, supplySet: set) -> bool:
        if item in supplySet:
            return True
        if item not in ingredientsOf:
            return False
        for ingredient in ingredientsOf[item]:
            if not self._canCreate(ingredient, ingredientsOf, supplySet):
                return False
        supplySet.add(item)
        return True

    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        supplySet = set(supplies)
        ingredientsOf = {}
        for i in range(len(recipes)):
            ingredientsOf[recipes[i]] = ingredients[i]

        validRecipes = []
        for recipe in recipes:
            if self._canCreate(recipe, ingredientsOf, supplySet):
                validRecipes.append(recipe)
        return validRecipes