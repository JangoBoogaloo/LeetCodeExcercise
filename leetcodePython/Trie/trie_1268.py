from typing import List
from trie_impl import Trie

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        trie = Trie()
        products.sort()
        for product in products:
            trie.insert(product)
        answer = []
        for i in range(1, len(searchWord)+1):
            answer.append(trie.wordsWithPrefix(searchWord[:i])[:3])
        return answer






