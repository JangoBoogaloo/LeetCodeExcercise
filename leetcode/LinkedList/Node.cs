namespace LinkedList;

public class Node
{
    public int val;
    public Node? next;
    public Node? random;
    
    public Node(int val) {
        this.val = val;
        next = null;
        random = null;
    }
}