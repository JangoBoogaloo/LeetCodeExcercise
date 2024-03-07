namespace LinkedListTests;

[TestFixture]
internal class LinkedList_237
{
    class Solution {
        public void DeleteNode(ListNode node) {
            node.val = node.next.val;
            node.next = node.next.next;
        }
    }
}