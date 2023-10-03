namespace LinkedListTests;

[TestFixture]
class LinkedList_23
{
    public class Solution {
        public ListNode MergeKLists(ListNode[] lists) {
            var pq = new PriorityQueue<ListNode, int>();
            foreach(var node in lists) {
                if(node is not null) pq.Enqueue(node, node.val);
            }
            var dummyHead = new ListNode(int.MinValue);
            var current = dummyHead;
            while (pq.Count > 0)
            {
                var minimum= pq.Dequeue();
                current.next = minimum;
                if(minimum.next is not null) pq.Enqueue(minimum.next, minimum.next.val);
                current = current.next;
            }
            return dummyHead.next;
        }
    }
}