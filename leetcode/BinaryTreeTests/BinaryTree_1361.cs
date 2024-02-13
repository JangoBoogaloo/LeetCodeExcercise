namespace BinaryTreeTests;

[TestFixture]
internal class BinaryTree_1361
{
    private class Solution {
        public bool ValidateBinaryTreeNodes(int n, int[] leftChild, int[] rightChild)
        {
            var root = FindRoot(n, leftChild, rightChild);
            if (root == -1) return false;
            var seen = new HashSet<int>();
            var stack = new Stack<int>();
            seen.Add(root);
            stack.Push(root);
            while (stack.Any())
            {
                var node = stack.Pop();
                var children = new [] { leftChild[node], rightChild[node] };
                foreach (var child in children) {
                    if(child == -1) continue;
                    if (seen.Contains(child))
                    {
                        return false;
                    }
                    stack.Push(child);
                    seen.Add(child);
                }
            }

            return seen.Count == n;
        }

        /// leftChild and rightChild: they are all child node.
        /// Within n if the data not in leftChild and rightChild. It suppose to be root.
        private int FindRoot(int n, int[] left, int[] right) {
            var children = new HashSet<int>();
            foreach (var node in left)
            {
                children.Add(node);
            }
            foreach (var node in right) {
                children.Add(node);
            }
    
            for (var i = 0; i < n; i++) {
                if (!children.Contains(i)) {
                    return i;
                }
            }
            return -1;
        }
    }
}
