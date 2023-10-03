namespace LinkedListTests;

[TestFixture]
class LinkedList_19
{
    class Solution {
        public ListNode RemoveNthFromEnd(ListNode head, int n) {
            var fast = head;
            for(var i=0; i<n; i++) {
                fast = fast.next;
            }
            var dummyHead = new ListNode(0);
            var slow =dummyHead;
            slow.next = head;
            while(fast is not null) {
                slow = slow.next;
                fast = fast.next;
            }
            slow.next = slow.next.next;
            return dummyHead.next;
        }
    }
    
}