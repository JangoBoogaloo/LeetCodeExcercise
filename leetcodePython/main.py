from TreeNode import TreeNode

if __name__ == "__main__":
    values = [1,None,3]
    tree = TreeNode.buildTree(values)
    data = TreeNode.toList(tree)
    print(data)