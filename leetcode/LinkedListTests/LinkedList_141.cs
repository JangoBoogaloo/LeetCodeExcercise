namespace LinkedListTests;

[TestFixture]
internal class LinkedList_141
{
    class Solution
    {
        public bool HasCycle(ListNode head)
        {
            var slow = head;
            var fast = head;
            while (fast is not null && fast.next is not null)
            {
                slow = slow.next;
                fast = fast.next.next;
                if (slow == fast) return true;
            }

            return false;
        }
    }
}