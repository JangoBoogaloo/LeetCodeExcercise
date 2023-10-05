namespace LinkedListTests;

[TestFixture]
public class Linkedlist_86
{
    private class Solution {
        public ListNode Partition(ListNode head, int x) {
            var smaller = new ListNode(-1);
            var greater = new ListNode(-1);
            var currS = smaller;
            var currG = greater;

            while(head is not null) {
                if(head.val < x) {
                    currS.next = head;
                    currS = currS.next;
                } else {
                    currG.next = head;
                    currG = currG.next;
                }
                var tmp = head.next;
                head.next = null;
                head = tmp;
            }
            currS.next = greater.next;
            return smaller.next;
        }
    }
}

