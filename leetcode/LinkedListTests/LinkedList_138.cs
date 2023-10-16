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
    
    class Solution_BigO1_Memory {
        public Node? CopyRandomList(Node? head) {
            if(head is null) return null;
            var curr = head;
            while (curr is not null)
            {
                var newNode = new Node(curr.val)
                {
                    next = curr.next
                };
                curr.next = newNode;
                curr = newNode.next;
            }

            curr = head;
            while (curr is not null)
            {
                if (curr.random is not null)
                {
                    curr.next.random = curr.random.next;
                }
                curr = curr.next.next;
            }

            var oldHead = head;
            var newHead = head.next;
            var result = newHead;
            while (oldHead is not null)
            {
                oldHead.next = oldHead.next.next;
                if (newHead.next is not null)
                {
                    newHead.next = newHead.next.next;
                }

                oldHead = oldHead.next;
                newHead = newHead.next;
            }

            return result;
        }
    }
}