namespace LinkedListTests;

[TestFixture]
internal class LinkedList_328
{
    class Solution {
        public ListNode OddEvenList(ListNode head) {
            if(head is null) return head;
            var odd = head;
            var even = head.next;
            var evenHead = even;
        
            while(even is not null && even.next is not null) {
                odd.next = even.next;
                odd = odd.next;
                even.next = odd.next;
                even = even.next;
            }
            odd.next = evenHead;
            return head;
        }
    }
}