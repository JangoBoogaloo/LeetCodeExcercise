import bisect
from typing import List


class SolutionBruteForce:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        search_key = ''
        ans = []
        products.sort()
        for ch in searchWord:
            search_key += ch
            match_count = 0
            match_list = []
            for product in products:
                if product.startswith(search_key):
                    match_list.append(product)
                    match_count += 1
                    if match_count == 3:
                        break
            ans.append(match_list)
        return ans


class SolutionBinarySearch:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        search_key = ''
        ans = []
        products.sort()
        for ch in searchWord:
            search_key += ch
            left = bisect.bisect_left(products, search_key)
            match_list = [w for w in products[left:left + 3] if w.startswith(search_key)]
            ans.append(match_list)
        return ans
