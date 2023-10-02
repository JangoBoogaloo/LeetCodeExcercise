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
}