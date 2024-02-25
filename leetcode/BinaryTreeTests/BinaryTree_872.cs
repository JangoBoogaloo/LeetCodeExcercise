namespace BinaryTreeTests;

[TestFixture]
internal class BinaryTree_872
{
    class Solution {
        public bool LeafSimilar(TreeNode root1, TreeNode root2) {
            var leafList = new List<int>();
            InOrderFirst(root1);
            var leafIndex = 0;
            var leafSame = true;
            InOrderSecond(root2);
            leafSame = leafSame && leafIndex == leafList.Count;
            return leafSame;

            void InOrderFirst(TreeNode root) {
                if(root is null) return;
                if(root.left is null && root.right is null) {
                    leafList.Add(root.val);
                    return;
                }
                InOrderFirst(root.left);
                InOrderFirst(root.right);
            }

            void InOrderSecond(TreeNode root) {
                if(root is null || !leafSame) return;
                if(root.left is null && root.right is null) {
                    if(leafIndex == leafList.Count) {
                        leafSame = false;
                        return;
                    }
                    if(leafList[leafIndex] != root.val) {
                        leafSame = false;
                        return;
                    }
                    leafIndex++;
                }
                InOrderSecond(root.left);
                InOrderSecond(root.right);
            }
        }
    }
}