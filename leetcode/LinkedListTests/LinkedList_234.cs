namespace LinkedListTests;

[TestFixture]
class LinkedList_234
{
    class Solution {
        public bool IsPalindrome(ListNode head) {
            var halfHead = EndOfFirstHalf(head).next;
            var reverseHalf = ReverseList(halfHead);
            while(reverseHalf is not null) {
                if(reverseHalf.val != head.val) {
                    return false;
                }
                head = head.next;
                reverseHalf = reverseHalf.next;
            }
            return true;
        }

        private ListNode ReverseList(ListNode head) {
            ListNode newHead = null;
            ListNode beforeNewHead = null;
            while (head is not null) {
                beforeNewHead = new ListNode(head.val);
                beforeNewHead.next = newHead;
                newHead = beforeNewHead;
                head = head.next;
            }
            return newHead;
        }

        private ListNode EndOfFirstHalf(ListNode head) {
            ListNode fast = head;
            ListNode slow = head;
            while (fast.next != null && fast.next.next != null) {
                fast = fast.next.next;
                slow = slow.next;
            }
            return slow;
        }
    }
}