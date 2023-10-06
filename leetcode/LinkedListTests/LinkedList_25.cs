namespace LinkedListTests;

[TestFixture]
class LinkedList_25
{
    class SolutionRecursive {
        public ListNode? ReverseKGroup(ListNode? head, int k) {
            if(head is null) return head;
            var end = head;
            for(var i=0; i < k; i++) {
                if(end == null) return head;
                end = end.next;
            }
            var newHead = Reverse(head, end);
            head.next = ReverseKGroup(end, k);
            return newHead;
        }

        private static ListNode? Reverse(ListNode? begin, ListNode? end) {
            ListNode? prev = null;
            var next = begin;
            while(begin !=end) {
                next = begin.next;
                begin.next = prev;
                prev = begin;
                begin = next;
            }
            return prev;
        }
    }
}

