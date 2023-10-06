namespace LinkedListTests;

[TestFixture]
class LinkedList_24
{
    class Solution {
        public ListNode SwapPairs(ListNode head) {
            var dummy = new ListNode(-1);
            dummy.next = head;
            var prev = dummy;
            while(head is not null && head.next is not null) {
                var first = head;
                var second = head.next;
                prev.next = second;
                first.next = second.next;
                second.next = first;
                prev = first;
                head = first.next;
            }
            return dummy.next;
        }
    }
}
