from typing import List
import Backtracking.bt_131, DynamicProgramming.dp_131
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        return []




import pytest

target = DynamicProgramming.dp_131.Solution()
testCases = [
    ("a", [["a"]]),
    ("aa", [["a", "a"], ["aa"]]),
    ("aaa", [["a", "a", "a"], ["a", "aa"], ["aa", "a"], ["aaa"]]),
]
@pytest.mark.parametrize("txt, expect", testCases)
def test_131_partion(txt, expect):
    actual = target.partition(txt)
    for a in actual:
        assert a in expect
    for e in expect:
        assert e in actual