using System.Text;

namespace BinaryTreeTests;

public class BinaryTree_2096
{
    class Solution {
        public string GetDirections(TreeNode root, int startValue, int destValue)
        {
            var startToAncestor = new StringBuilder();
            var destToAncestor = new StringBuilder();
            
            //After the 2 methods call below, the string builder represent
            // start ->....-> root
            // dest ->....-> root
            CheckValueExistDfs(root, startValue, startToAncestor);
            CheckValueExistDfs(root, destValue, destToAncestor);
            
            //After the 2 methods call below, the string builder represent
            // start ->....-> lca
            // dest ->....-> lca
            RemoveCommonPath(startToAncestor, destToAncestor);
            ReverseStringBuilder(startToAncestor);
            ReverseStringBuilder(destToAncestor);
            startToAncestor.Replace('R', 'U');
            startToAncestor.Replace('L', 'U');
            return startToAncestor.Append(destToAncestor).ToString();
        }

        /// <summary>
        /// Remove the path from root to lowest common ancestor
        /// </summary>
        private void RemoveCommonPath(StringBuilder startToRoot, StringBuilder destToRoot)
        {
            while(startToRoot.Length > 0 && destToRoot.Length > 0 && startToRoot[^1] == destToRoot[^1])
            {
                startToRoot.Remove(startToRoot.Length - 1, 1);
                destToRoot.Remove(destToRoot.Length - 1, 1);
            }
        }

        private void ReverseStringBuilder(StringBuilder path){
            for(var i = 0; i < path.Length / 2; i++){
                (path[path.Length - i - 1], path[i]) = (path[i], path[path.Length - i - 1]);
            }
        }
        private bool CheckValueExistDfs(TreeNode? node, int value, StringBuilder targetToRoot)
        {
            //We reach end of this path
            if (node is null) return false;
            if (node.val == value) return true;

            var isInLeft = CheckValueExistDfs(node.left, value, targetToRoot);
            if (isInLeft)
            {
                targetToRoot.Append("L");
                return true;
            }
            var isInRight = CheckValueExistDfs(node.right, value, targetToRoot);
            if (isInRight)
            {
                targetToRoot.Append("R");
                return true;
            }
            return false;
        }
    }
}

