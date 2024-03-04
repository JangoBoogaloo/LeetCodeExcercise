namespace LinkedListTests;

[TestFixture]
internal class LinkedList_146
{
    class LRUCache
    {
        private IDictionary<int, DLinkNode> _keyValueMap;
        private readonly int _capacity;
        private DLinkNode _head;
        private DLinkNode _tail;
        public LRUCache(int capacity)
        {
            _keyValueMap = new Dictionary<int, DLinkNode>();
            _capacity = capacity;
            _head = new DLinkNode();
            _tail = new DLinkNode();
            _head.Next = _tail;
            _tail.Prev = _head;
        }
    
        public int Get(int key)
        {
            _keyValueMap.TryGetValue(key, out var node);
            if (node is null) return -1;
            RemoveNode(node);
            AddNodeToFront(node);
            return node.Value;
        }
    
        public void Put(int key, int value) {
            _keyValueMap.TryGetValue(key, out var node);
            if (node is not null)
            {
                node.Value = value;
                RemoveNode(node);
                AddNodeToFront(node);
                return;
            }
    
            node = new DLinkNode(key, value);
            _keyValueMap[key] = node;
            AddNodeToFront(node);
            if (_keyValueMap.Count > _capacity)
            {
                var end = _tail.Prev;
                RemoveNode(end);
                _keyValueMap.Remove(end.Key);
            }
        }
    
        private class DLinkNode
        {
            public int Key;
            public int Value;
            public DLinkNode Next;
            public DLinkNode Prev;
    
            public DLinkNode(int key=0, int value=0, DLinkNode next = null, DLinkNode prev = null)
            {
                this.Key = key;
                this.Value = value;
                this.Next = next;
                this.Prev = prev;
            }
        }
    
        private void AddNodeToFront(DLinkNode node)
        {
            node.Prev = _head;
            node.Next = _head.Next;
            _head.Next.Prev = node;
            _head.Next = node;
        }
    
        private void RemoveNode(DLinkNode node)
        {
            var prev = node.Prev;
            var next = node.Next;
            prev.Next = next;
            next.Prev = prev;
        }
    }
}

