namespace LinkedListTests;

public class LInkedList_92
{
    class Solution {
        public ListNode ReverseBetween(ListNode head, int left, int right) {
            if(head is null) return head;

            var leftNode = head;
            ListNode? beforeLeft = null;
            right -= left;
            left--;
            while(leftNode is not null && left >0) {
                beforeLeft = leftNode;
                leftNode = leftNode.next;
                left--;
            }
            var curr  = leftNode;
            ListNode? prev = null;
            while(curr is not null && right > -1) {
                var nextTmp = curr.next;
                curr.next = prev;
                prev = curr;
                curr = nextTmp;
                right--;
            }
            if(beforeLeft is not null) {
                beforeLeft.next = prev;
            } else {
                head = prev;
            }
            leftNode.next = curr;
            return head;
        }
    }
}