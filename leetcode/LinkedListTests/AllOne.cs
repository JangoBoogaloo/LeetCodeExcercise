namespace LinkedListTests;

//https://leetcode.com/problems/all-oone-data-structure/description/
internal class AllOne
{
    private Dictionary<string, int> _keyCountMap;
    private Dictionary<int, Node> _countNodeMap;

    private Node _head;
    private Node _tail;
    
    public AllOne()
    {
        _keyCountMap = new Dictionary<string, int>();
        _countNodeMap = new Dictionary<int, Node>();
        _head = new Node(int.MinValue);
        _tail = new Node(int.MaxValue);
        _head.Next = _tail;
        _tail.Prev = _head;
    }
    
    public void Inc(string key) {
        if (_keyCountMap.TryGetValue(key, out var count))
        {
            var prevNode = _countNodeMap[count];
            prevNode.Keys.Remove(key);
            if (!_countNodeMap.ContainsKey(count + 1))
            {
                AddNodeAfter(new Node(count + 1), prevNode);
            }
            _countNodeMap[count + 1].Keys.Add(key);
            _keyCountMap[key]++;
            if (prevNode.Keys.Count == 0)
            {
                Remove(prevNode);
                _countNodeMap.Remove(count);
            }
        }
        else
        {
            _keyCountMap[key] = 1;
            if (!_countNodeMap.ContainsKey(1))
            {
                AddNodeAfter(new Node(1), _head);
            }
            _countNodeMap[1].Keys.Add(key);
        }
    }
    
    public void Dec(string key)
    {
        var count = 0;
        if (_keyCountMap.ContainsKey(key))
        {
            count = _keyCountMap[key];
            var node = _countNodeMap[count];
            node.Keys.Remove(key);
            if (count == 1)
            {
                _keyCountMap.Remove(key);
            }
            else
            {
                if (!_countNodeMap.ContainsKey(count - 1))
                {
                    AddNodeAfter(new Node(count-1), node.Prev);
                }

                _countNodeMap[count - 1].Keys.Add(key);
                _keyCountMap[key]--;
            }

            if (node.Keys.Count == 0)
            {
                Remove(node);
                _countNodeMap.Remove(node.Count);
            }
        }
        
    }
    
    public string GetMaxKey()
    {
        if (_tail.Prev == _head) return "";
        return _tail.Prev.Keys.First();
    }
    
    public string GetMinKey()
    {
        if (_head.Next == _tail) return "";
        return _head.Next.Keys.First();
    }

    private void AddNodeAfter(Node newNode, Node prev)
    {
        newNode.Prev = prev;
        newNode.Next = prev.Next;
        prev.Next.Prev = newNode;
        prev.Next = newNode;
        _countNodeMap[newNode.Count] = newNode;
    }

    private void Remove(Node newNode)
    {
        var prev = newNode.Prev;
        var next = newNode.Next;
        prev.Next = next;
        next.Prev = prev;
    }

    private class Node
    {
        public int Count;
        public HashSet<string> Keys;
        public Node Prev, Next;

        public Node(int count)
        {
            Count = count;
            Keys = new HashSet<string>();
        }
    }
}