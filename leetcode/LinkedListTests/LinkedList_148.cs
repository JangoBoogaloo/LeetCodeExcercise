namespace LinkedListTests;

[TestFixture]
internal class LinkedList_148
{
    private class Solution {
        public ListNode? SortList(ListNode? head)
        {
            if (head is null || head.next is null) return head;
            var midNode = GetAndBreakMiddle(head);
            var list1 = SortList(head);
            var list2 = SortList(midNode);
            var list = MergeList(list1, list2);
            return list;
        }
    
        private ListNode GetAndBreakMiddle(ListNode head)
        {
            ListNode? beforeMid = null;
            var fast = head;
            var slow = head;
            //a1->a2
            //beforeMid = a1
            //slow = a2
            while (fast is not null && fast.next is not null)
            {
                beforeMid = slow;
                slow = slow.next;
                fast = fast.next.next;
            }
    
            beforeMid.next = null;
            return slow;
        }
    
        private ListNode MergeList(ListNode node1, ListNode node2)
        {
            var dummy = new ListNode();
            var curr = dummy;
            while (node1 is not null && node2 is not null)
            {
                if (node1.val < node2.val)
                {
                    curr.next = node1;
                    node1 = node1.next;
                }
                else
                {
                    curr.next = node2;
                    node2 = node2.next;
                }
                curr = curr.next;
            }
    
            if (node1 is null)
            {
                curr.next = node2;
            }
            else
            {
                curr.next = node1;
            }
    
            return dummy.next;
        }
    }
}