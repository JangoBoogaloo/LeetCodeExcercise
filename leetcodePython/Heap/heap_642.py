import heapq
from typing import List
from collections import defaultdict


class TrieNode:
    def __init__(self):
        self.children = {}
        self.sentence_count = defaultdict(int)


class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        self.root = TrieNode()
        for sentence, count in zip(sentences, times):
            self.add_to_trie(sentence, count)
        self.curr_sentence_ch_arr = []
        self.curr_node = self.root
        self.end = TrieNode()

    def add_to_trie(self, sentence, count):
        node = self.root
        for ch in sentence:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
            node.sentence_count[sentence] -= count

    def input(self, c: str) -> List[str]:
        # reaching the end, user knows what he wants, no more suggestion
        if c == "#":
            curr_sentence = "".join(self.curr_sentence_ch_arr)
            self.add_to_trie(curr_sentence, 1)
            self.curr_sentence_ch_arr = []
            self.curr_node = self.root
            return []

        self.curr_sentence_ch_arr.append(c)

        # no matching
        if c not in self.curr_node.children:
            self.curr_node = self.end
            return []

        self.curr_node = self.curr_node.children[c]
        sentence_count = self.curr_node.sentence_count
        items = [(val, key) for key, val in self.curr_node.sentence_count.items()]
        ans = heapq.nsmallest(3, items)
        return [a[1] for a in ans]


# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)

if __name__ == "__main__":
    system = AutocompleteSystem(["i love you", "island", "iroman", "i love leetcode"], [5, 3, 2, 2])
    print(system.input("i"))
    print(system.input(" "))
    print(system.input("a"))
    print(system.input("b"))
    print(system.input("#"))
    a = (-3, 'a')
    print((lambda x: (a[0], a[1])))
