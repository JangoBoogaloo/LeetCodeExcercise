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
        self.curr_sentence = []
        self.curr_node = self.root
        self.end = TrieNode()

    def add_to_trie(self, sentence, count):
        node = self.root
        for ch in sentence:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
            node.sentence_count[sentence] += count


    def input(self, c: str) -> List[str]:
        # reaching the end
        if c == "#":
            curr_sentence = "".join(self.curr_sentence)
            self.add_to_trie(curr_sentence, 1)
            self.curr_sentence = []
            self.curr_node = self.root
            return []

        self.curr_sentence.append(c)

        # no matching
        if c not in self.curr_node.children:
            self.curr_node = self.end
            return []

        self.curr_node = self.curr_node.children[c]
        sentence_count = self.curr_node.sentence_count
        sorted_sentence_count = sorted(sentence_count.items(), key=lambda x: (-x[1], x[0]))

        ans = []
        for i in range(min(3, len(sorted_sentence_count))):
            ans.append(sorted_sentence_count[i][0])
        return ans

# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)