﻿namespace BinaryTreeTests;

[TestFixture]
internal class BinaryTree_968
{
    private class Solution
    {
        private const int Leaf = 0;
        private const int Camera = 1;
        private const int Covered = 2;

        public int MinCameraCover(TreeNode root)
        {
            var answer = 0;
            var state = Dfs(root);
            if (state == Leaf) answer++;
            return answer;
        
            int Dfs(TreeNode node)
            {
                if (node is null) return Covered;

                var leftState = Dfs(node.left);
                var rightState = Dfs(node.right);

                //  
                //      node <-----camera
                //  leaf    leaf
                if (leftState == Leaf || rightState == Leaf)
                {
                    answer++;
                    return Camera;
                }
                //  
                //      node <-----covered
                //  camera    camera 
                else if (leftState == Camera || rightState == Camera)
                {
                    return Covered;
                }
                //  
                //       node <-----leaf
                //  cover    cover  
                else {
                    return Leaf;
                }
            }
        }
    }
}