namespace LinkedListTests;

internal class MaxStack
{
    class MaxComparer : IComparer<int>{
        public int Compare(int a, int b){
            return b-a;
        }
    }
    
    private SortedDictionary<int, List<DNode>> _valueListMap;
    private DNode _head;
    private DNode _tail;
    public MaxStack()
    {
        _valueListMap = new SortedDictionary<int, List<DNode>>(new MaxComparer());
        _head = new DNode();
        _tail = new DNode();
        _head.Next = _tail;
        _tail.Prev = _head;
    }
    
    public void Push(int x)
    {
        var node = new DNode(x);
        if (!_valueListMap.ContainsKey(x))
        {
            _valueListMap[x] = new List<DNode>();
        }
        _valueListMap[x].Add(node);
        var last = _tail.Prev;
        
        last.Next = node;
        node.Prev = last;
        
        node.Next = _tail;
        _tail.Prev = node;
    }
    
    public int Pop()
    {
        var last = _tail.Prev;
        if (last == _head)
        {
            throw new InvalidOperationException("Empty Stack. Can not Pop");
        }

        last.Prev.Next = _tail;
        _tail.Prev = last.Prev;
        var valueList = _valueListMap[last.Val];
        //remove the last added item
        valueList.RemoveAt(valueList.Count-1);
        if (valueList.Count == 0)
        {
            _valueListMap.Remove(last.Val);
        }

        return last.Val;
    }
    
    public int Top() {
        var last = _tail.Prev;
        if (last == _head)
        {
            throw new InvalidOperationException("Empty Stack. Can not Top");
        }

        return last.Val;
    }
    
    public int PeekMax()
    {
        return _valueListMap.First().Value[0].Val;
    }
    
    public int PopMax()
    {
        var maxValueList = _valueListMap.First().Value;
        var lastNode = maxValueList[maxValueList.Count - 1];
        maxValueList.RemoveAt(maxValueList.Count - 1);
        if (maxValueList.Count == 0)
        {
            _valueListMap.Remove(lastNode.Val);
        }

        lastNode.Prev.Next = lastNode.Next;
        lastNode.Next.Prev = lastNode.Prev;

        return lastNode.Val;
    }
    
    private class DNode
    {
        public int Val;
        public DNode? Prev;
        public DNode? Next;

        public DNode(int val = -1)
        {
            Val = val;
            Prev = null;
            Next = null;
        }
    }
}