namespace LinkedListTests;

[TestFixture]
internal class LinkedList_82
{
    class Solution {
        public ListNode DeleteDuplicates(ListNode head) {
            if(head is null) return head;
            var dummyHead = new ListNode(-101);
            dummyHead.next = head;
            var lastUnique = dummyHead;
            while(head is not null) {
                //this is duplicate
                if(head.next is not null && head.val == head.next.val) {
                    while(head.next is not null && head.val == head.next.val)
                    {
                        head = head.next;
                    }
                    lastUnique.next = head.next;
                } else {
                    lastUnique = lastUnique.next;
                }
                head = head.next;
            }
            return dummyHead.next;
        }
    }
}