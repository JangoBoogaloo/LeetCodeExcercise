using System.Text;

namespace BinaryTreeTests;

public class BinaryTree_2096
{
    class Solution {
        public string GetDirections(TreeNode root, int startValue, int destValue)
        {
            var startToRoot = new StringBuilder();
            var destToRoot = new StringBuilder();
            CheckValueExistDfs(root, startValue, startToRoot);
            CheckValueExistDfs(root, destValue, destToRoot);
            RemoveCommonPath(startToRoot, destToRoot);
            ReverseStringBuilder(startToRoot);
            ReverseStringBuilder(destToRoot);
            startToRoot.Replace('R', 'U');
            startToRoot.Replace('L', 'U');
            return startToRoot.Append(destToRoot).ToString();
        }

        /// <summary>
        /// </summary>
        /// <param name="startToRoot"></param>
        /// <param name="destToRoot"></param>
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

