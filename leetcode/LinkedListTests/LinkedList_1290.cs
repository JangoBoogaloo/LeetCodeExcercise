namespace LinkedListTests;

[TestFixture]
internal class LinkedList_1290
{
    private class Solution {
        public int GetDecimalValue(ListNode head) {
            var sum = 0;
            while(head is not null) {
                var data = head.val;
                sum = sum*2+data;
                head = head.next;
            }
            return sum;
        }
    }
}