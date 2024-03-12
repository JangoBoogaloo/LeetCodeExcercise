namespace LinkedListTests;

public class LinkedList_61
{
    class Solution {
        public ListNode RotateRight(ListNode head, int k) {
            if(head is null || head.next is null) return head;
            var tail = head;
            ListNode beforeTail = null;
            var nodeCount = 1;
            //A1->A2->A3->nil
            //
            while(tail.next is not null) {
                beforeTail = tail;
                tail = tail.next;
                nodeCount++;
            }
            var move = k%nodeCount;
            if(move ==0) return head;

            tail.next = head;

            //A1->.......An
            //0   A1->.......An
            //1   An->A1->.......An-1       from head we need to move n-1
            //2   An-1->An->A1->......An-2  from head we need to move n-2
            //k   An-k->............An-k-1  from head we need to move n-k
            for(var i=1; i<nodeCount-move; i++) {
                head = head.next;
            }
            var newHead = head.next;
            head.next = null;
            return newHead;
        }
    }
}