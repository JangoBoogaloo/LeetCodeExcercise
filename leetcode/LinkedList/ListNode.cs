namespace LinkedList;

public class ListNode
{
    public int val;
    public ListNode? next;

    public ListNode(int x)
    {
        val = x;
        next = null;
    }

    public static (ListNode?, ListNode?) ConstructCycle(int [] data, int cycleIndex)
    {
        if (data.Length == 0) return (null, null);
        var head = new ListNode(data[0]);
        var current = head;
        ListNode? cycleNode = null;
        for (var i = 1; i < data.Length; i++)
        {
            current.next = new ListNode(data[i]);
            current = current.next;
            if (i == cycleIndex) cycleNode = current;
        }
        current.next = cycleNode;
        return (head,cycleNode);
    }

    public static (ListNode?, ListNode?, ListNode?) ConstructIntersectNodes(int[] aList, int[] bList, int[] intersect)
    {
        var aHead = ConstructLinkedList(aList);
        var aTail = GetLast(aHead);
        var bHead = ConstructLinkedList(bList);
        var bTail = GetLast(bHead);
        var intersectHead = ConstructLinkedList(intersect);
        aTail.next = intersectHead;
        bTail.next = intersectHead;
        return (aHead, bHead, intersectHead);
    }

    private static ListNode? ConstructLinkedList(IReadOnlyList<int> data)
    {
        if (data.Count == 0)
        {
            return null;
        }
        var head = new ListNode(data[0]);
        var curr = head;
        for (var i = 1; i < data.Count; i++)
        {
            curr.next = new ListNode(data[i]);
            curr = curr.next;
        }

        return head;
    }

    private static ListNode? GetLast(ListNode? head)
    {
        if (head is null) return null;
        while (head is not null)
        {
            if (head.next is null) return head;
            head = head.next;
        }
        return null;
    }
}