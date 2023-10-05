namespace LinkedListTests;

[TestFixture]
class LinkedList_206
{
    private class SolutionRecursion {
        public ListNode? ReverseList(ListNode? head) {
            if(head is null || head.next is null) { 
                return head; 
            }
            var last = ReverseList(head.next);
            head.next.next = head;
            head.next = null;
            return last;
        }
    }
    
    private class SolutionIterative {
        public ListNode? ReverseList(ListNode? head)
        {
            ListNode? prev = null;
            var curr = head;
            while (curr is not null)
            {
                var nextTmp = curr.next;
                curr.next = prev;
                prev = curr;
                curr = nextTmp;
            }
            return prev;
        }
    }
}