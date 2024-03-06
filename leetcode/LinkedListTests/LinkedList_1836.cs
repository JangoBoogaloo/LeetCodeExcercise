namespace LinkedListTests;

public class LinkedList_1836
{
    class Solution {
        public ListNode DeleteDuplicatesUnsorted(ListNode head) {
            var valueFrequencyMap = new Dictionary<int, int>();
            var fakeHead = new ListNode();
            fakeHead.next = head;
            while(head is not null) {
                if(!valueFrequencyMap.ContainsKey(head.val)) {
                    valueFrequencyMap[head.val] = 0;
                }
                valueFrequencyMap[head.val]++;
                head = head.next;
            }

            var prev = fakeHead;
            var curr = fakeHead.next;
            while(curr is not null) {
                if(valueFrequencyMap[curr.val] > 1) {
                    prev.next = curr.next;
                    curr.next = null;
                    curr = prev;
                }
                prev = curr;
                curr = curr.next;
            }
            return fakeHead.next;
        }
    }
}
