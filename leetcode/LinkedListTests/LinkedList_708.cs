namespace LinkedListTests;

[TestFixture]
internal class LinkedList_708
{
    private class Solution {
        public Node Insert(Node head, int insertVal) {
            if(head is null) {
                head = new Node(insertVal);
                head.next = head;
                return head;
            }
            var curr = head;
            while(curr.next != head) {
                if(curr.val <= curr.next.val) {
                    //curr < insert < next
                    if(curr.val <= insertVal && curr.next.val >= insertVal) {
                        break;
                    }
                } else {
                    //curr >= next, insert > curr or insert < next
                    if(curr.val <= insertVal || curr.next.val >= insertVal) {
                        break;
                    }
                }
                curr = curr.next;
            }
            //curr->insert->next
            var node = new Node(insertVal);
            node.next = curr.next;
            curr.next = node;
            return head;
        }
    }
}