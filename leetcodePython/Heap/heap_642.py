import heapq
from bisect import bisect_left
from typing import List
from collections import defaultdict


class TrieNode:
    def __init__(self):
        self.children = {}
        self.sentence_count = defaultdict(int)


class AutocompleteSystemTrie:

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


class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        self.count = {s: t for t, s in zip(times, sentences)}
        self.rankings = sorted((-t, s) for t, s in zip(times, sentences))
        self._reset_curr()

    def _reset_curr(self):
        self.curr_input = []
        self.curr_ranks = [s for _, s in self.rankings]

    def input(self, c: str) -> List[str]:
        if c == "#":
            new_s = ''.join(self.curr_input)
            if new_s in self.count:
                rm_idx = bisect_left(self.rankings, (-self.count[new_s], new_s))
                self.rankings.pop(rm_idx)
            else:
                self.count[new_s] = 0
            self.count[new_s] += 1

            new_ranking = (-self.count[new_s], new_s)
            self.rankings.insert(bisect_left(self.rankings, new_ranking), new_ranking)

            self._reset_curr()
            return []
        else:
            self.curr_input.append(c)
            c_idx = len(self.curr_input) - 1
            self.curr_ranks = [s for s in self.curr_ranks if len(s) > c_idx and s[c_idx] == c]
            return self.curr_ranks[: 3]


if __name__ == "__main__":
    system = AutocompleteSystemTrie(["i love you", "island", "iroman", "i love leetcode"], [5, 3, 2, 2])
    print(system.input("i"))
    print(system.input(" "))
    print(system.input("a"))
    print(system.input("b"))
    print(system.input("#"))
    a = (-3, 'a')
    print((lambda x: (a[0], a[1])))
