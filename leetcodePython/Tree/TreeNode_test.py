import unittest

from TreeNode import TreeNode

class TestTreeNode(unittest.TestCase):
    def getTreeList(self, expected):
        tree = TreeNode.buildTree(expected)
        actual = TreeNode.toList(tree)
        return actual

    def test_buildTree(self):
        expected = [1, 2]
        self.assertListEqual(self.getTreeList(expected), expected)
        expected = [1, None, 3]
        self.assertListEqual(self.getTreeList(expected), expected)
        expected = [1, 2, 3, 4]
        self.assertListEqual(self.getTreeList(expected), expected)
        expected = [1, 2, None, 4]
        self.assertListEqual(self.getTreeList(expected), expected)
        expected = [1, 2, None, None, 5]
        self.assertListEqual(self.getTreeList(expected), expected)
        expected = [1, None, 3, None, None, 6, 7]
        self.assertListEqual(self.getTreeList(expected), expected)

if __name__ == "__main__":
    unittest.main()