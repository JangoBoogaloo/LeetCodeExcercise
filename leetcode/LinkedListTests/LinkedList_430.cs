namespace LinkedListTests;

[TestFixture]
internal class LinkedList_430
{
    class Node {
        public int val;
        public Node prev;
        public Node next;
        public Node child;
    }

    class Solution {
        public Node Flatten(Node head) {
            if(head is null) return head;
            var (resultHead, resultTail) = FlattenRecursive(head);
            return resultHead;
        }

        private (Node, Node) FlattenRecursive(Node node) {
            Node childHead = null;
            Node childTail = null;
            Node nextHead = null;
            Node nextTail = null;
            if(node.next is not null) {
                (nextHead, nextTail) = FlattenRecursive(node.next);
            }
            if(node.child is not null) {
                (childHead, childTail) = FlattenRecursive(node.child);
                node.child = null;
            }

            //if there's a child
            if(childHead is not null) {
                node.next = childHead;
                childHead.prev = node;
                //If there's a next
                if(nextHead is not null) {
                    childTail.next = nextHead;
                    nextHead.prev = childTail;
                    return (node, nextTail);
                }
                return (node, childTail);
            }
            //If there's a next 
            if(nextHead is not null) {
                node.next = nextHead;
                nextHead.prev = node;
                return (node, nextTail);
            }
            return (node, node);
        }
    }
}