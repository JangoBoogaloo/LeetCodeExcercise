namespace LinkedListTests;

public class LinkedList_83
{
    class Solution {
        public ListNode? DeleteDuplicates(ListNode? head) {
            if(head is null) return head;

            var slow = head;
            var fast = head.next;
            while(fast is not null) {
                if(fast.val != slow.val) {
                    slow.next = fast;
                    slow = slow.next;
                }
                fast = fast.next;
            }
            slow.next = null;
            return head;
        }
    }
}