namespace GraphTests;

[TestFixture]
class Graph_797
{
    class Solution {
        public IList<IList<int>> AllPathsSourceTarget(int[][] graph) {
            var paths = new List<IList<int>>();
            var currentPath = new List<int>();
            Traverse(0);
            return paths;
            void Traverse(int source) {
                currentPath.Add(source);
                if(source == graph.Length -1) {
                    paths.Add(new List<int>(currentPath));
                    currentPath.RemoveAt(currentPath.Count-1);
                    return;
                }
                foreach(var v in graph[source]) {
                    Traverse(v);
                }
                currentPath.RemoveAt(currentPath.Count-1);
            }
        }
    }
}
