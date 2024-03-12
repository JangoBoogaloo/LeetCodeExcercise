namespace LinkedListTests;

[TestFixture]
internal class LinkedList_203
{
    private class Solution {
        public ListNode RemoveElements(ListNode head, int val) {
            var dummyHead = new ListNode();
            var prev = dummyHead;
            var curr = head;
            prev.next = curr;
            while(curr is not null) {
                //prev->curr->next
                //prev->next
                if(curr.val == val) {
                    prev.next = curr.next;
                } else {
                    prev = prev.next;
                }
                curr = curr.next;            
            }
            return dummyHead.next;
        }
    }
}