namespace LinkedListTests;

[TestFixture]
class LinkedList_138
{
    class Solution {
        public Node? CopyRandomList(Node? head) {
            if(head is null) return null;
            var visited = new Dictionary<Node, Node?>();
            visited[head] = new Node(head.val);
            var newHead = visited[head];
            var curr = newHead;
            while(head is not null) {
                curr!.random = GetClonedNode(head.random);
                curr.next = GetClonedNode(head.next);
                curr = curr.next;
                head = head.next;
            }
            return newHead;

            Node? GetClonedNode(Node? node) {
                if(node is null) return null;

                if(visited.TryGetValue(node, out var clonedNode)) {
                    return clonedNode;
                }

                visited[node] = new Node(node.val);
                return visited[node];
            }
        }
    }
}