from typing import List


class Solution:
    def _canCreate(self, item: str, ingredientsOf, supplySet: set, visited: set) -> bool:
        if item in supplySet:
            return True
        if item not in ingredientsOf:
            return False
        if item in visited:
            return False
        visited.add(item)
        for ingredient in ingredientsOf[item]:
            if not self._canCreate(ingredient, ingredientsOf, supplySet, visited):
                return False
        supplySet.add(item)
        return True

    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        supplySet = set(supplies)
        ingredientsOf = {}
        visited = set()
        for i in range(len(recipes)):
            ingredientsOf[recipes[i]] = ingredients[i]

        validRecipes = []
        for recipe in recipes:
            if self._canCreate(recipe, ingredientsOf, supplySet, visited):
                validRecipes.append(recipe)
        return validRecipes








import pytest
target = Solution()

@pytest.mark.parametrize("recipes, ingredients, supplies, expect",
[
    (["a", "b"], [["c"], ["d"]], ["c", "d"], ["a", "b"]),
    (["a", "b"], [["c"], ["d"]], ["c", "e"], ["a"]),
    (["a", "b"], [["b"], ["a"]], ["a"], ["a", "b"]),
    (["a", "b"], [["b", "c"], ["a", "c"]], ["c"], []),
])
def test_findAllRecipes(recipes, ingredients, supplies, expect):
    print(target.findAllRecipes(recipes, ingredients, supplies))
    assert target.findAllRecipes(recipes, ingredients, supplies) == expect