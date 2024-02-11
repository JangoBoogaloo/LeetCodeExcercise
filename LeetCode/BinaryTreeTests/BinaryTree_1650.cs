namespace BinaryTreeTests;

[TestFixture]
internal class BinaryTree_1650
{
    class Node {
        public int val;
        public Node left;
        public Node right;
        public Node parent;
    }

    class Solution
    {
        public Node LowestCommonAncestor(Node p, Node q)
        {
            var tempA = p;
            var tempB = q;
            while (tempA != tempB)
            {
                if (tempA is null) tempA = q;
                else tempA = tempA.parent;
                if (tempB is null) tempB = p;
                else tempB = tempB.parent;
            }

            return tempA;
        }
    }
}


