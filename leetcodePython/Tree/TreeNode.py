from collections import deque

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val=val
        self.left = left
        self.right=right

    @staticmethod
    def buildTree(values):
        if not len(values):
            return None
        root = TreeNode(values[0])
        nodes = deque()
        nodes.append(root)
        i=1
        while i < len(values):
            node = nodes.popleft()
            if node is None:
                i += 2
                continue
            if values[i] is None:
                node.left = None
            else:
                node.left = TreeNode(values[i])
            nodes.append(node.left)
            i += 1
            if values[i] is None:
                node.right = None
            else:
                node.right = TreeNode(values[i])
            nodes.append(node.right)
            i += 1
        return root

    @staticmethod
    def toList(root):
        result = []
        if root is None:
            return result
        nodes = deque()
        nodes.append(root)
        nonNullExist = True
        while nonNullExist:
            nodeCount = len(nodes)
            nonNullExist = False
            for i in range(nodeCount):
                node = nodes.popleft()
                if node is None:
                    result.append(None)
                    nodes.append(None)
                    nodes.append(None)
                else:
                    nonNullExist = True
                    result.append(node.val)
                    nodes.append(node.left)
                    nodes.append(node.right)
        for t in reversed(range(len(result))):
            if result[t] is not None:
                break
            result.pop(t)

        return result