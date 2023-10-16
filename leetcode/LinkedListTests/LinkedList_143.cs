namespace LinkedListTests;

[TestFixture]
class LinkedList_143
{
    class Solution {
        public void ReorderList(ListNode head) {
            var middle = GetMiddle(head);
            var reverseHead = Reverse(middle.next);
            middle.next = null;
            AdjacentMerge(head, reverseHead);

            void AdjacentMerge(ListNode head1, ListNode head2) {
                var curr1 = head1;
                var curr2 = head2;
            
                while(curr1 is not null && curr2 is not null) {
                    var next1 = curr1.next;
                    var next2 = curr2.next;
                    curr1.next = curr2;
                    curr2.next = next1;
                    curr1 = next1;
                    curr2 = next2;
                }
            }

            ListNode Reverse(ListNode node) {
                ListNode prev = null;
                var curr = node;
                while(curr is not null) {
                    var tmpNext = curr.next;
                    curr.next = prev;
                    prev = curr;
                    curr = tmpNext;
                }
                return prev;
            }

            ListNode GetMiddle(ListNode node) {
                var slow = node;
                var fast = node;
                while (fast is not null && fast.next is not null)
                {
                    fast = fast.next.next;
                    slow = slow.next;
                }
                return slow;
            }
        }
    }
}