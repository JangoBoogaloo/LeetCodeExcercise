namespace LinkedListTests;

[TestFixture]
internal class LinkedList_460
{
    private class LFUCache
    {
        private IDictionary<int, LinkedList<Data>> _countDictionary;
        private IDictionary<int, LinkedListNode<Data>> _dataNodeDictionary;
        private int _cacheSize;
        private int _minAccessCount;
        private readonly int Capacity;
        
        public LFUCache(int capacity)
        {
            _countDictionary = new Dictionary<int, LinkedList<Data>>();
            _dataNodeDictionary = new Dictionary<int, LinkedListNode<Data>>();
            Capacity = capacity;
            _cacheSize = 0;
            _minAccessCount = 1;
        }
        
        public int Get(int key)
        {
            if (!_dataNodeDictionary.TryGetValue(key, out var dataNode))
            {
                return -1;
            }

            UpdateNodeCountAndFrequency(dataNode);
            return dataNode!.Value.Value;
        }
        
        public void Put(int key, int value)
        {
            if (Capacity == 0) return;
            if (_dataNodeDictionary.TryGetValue(key, out var dataNode))
            {
                dataNode.Value.Value = value;
                UpdateNodeCountAndFrequency(dataNode);
                return;
            }

            if (_cacheSize == Capacity)
            {
                RemoveLeastFrequentRecentData();
            }

            //Brand new put, so its access frequency/count is 1
            _minAccessCount = 1;
            LinkedList<Data> sameAccessList;
            if (_countDictionary.TryGetValue(_minAccessCount, out var existingList))
            {
                sameAccessList = existingList;
            }
            else
            {
                sameAccessList = new LinkedList<Data>();
                _countDictionary.Add(_minAccessCount, sameAccessList);
            }
            var node = new LinkedListNode<Data>(new Data() { Key = key, Value = value, AccessCount = 1 });
            //put this data in the 1 time access list
            sameAccessList.AddFirst(new Data() { Key = key, Value = value, AccessCount = 1 });
            _dataNodeDictionary[key] = sameAccessList.First;
            _cacheSize++;
        }

        private void RemoveLeastFrequentRecentData()
        {
            var leastFrequentList = _countDictionary[_minAccessCount];
            _dataNodeDictionary.Remove(leastFrequentList.Last!.Value.Key);
            leastFrequentList.RemoveLast();
            _cacheSize--;
        }

        private void UpdateNodeCountAndFrequency(LinkedListNode<Data> dataNode)
        {
            var sameCountDataNodeList = _countDictionary[dataNode.Value.AccessCount];
            sameCountDataNodeList.Remove(dataNode);
            
            //The data has min access count and it is the only one, so now the min access count increase
            if (!sameCountDataNodeList.Any() && dataNode.Value.AccessCount == _minAccessCount)
            {
                _minAccessCount++;
            }
            dataNode.Value.AccessCount++;
            LinkedList<Data> sameCountList;
            if (_countDictionary.TryGetValue(dataNode.Value.AccessCount, out var existingList))
            {
                sameCountList = existingList;
            }
            else
            {
                sameCountList = new LinkedList<Data>();
                _countDictionary[dataNode.Value.AccessCount] = sameCountList;
            }
            sameCountList.AddFirst(dataNode.Value);
            _dataNodeDictionary[dataNode.Value.Key] = sameCountList.First;
        }

        private class Data
        {
            public int Key;
            public int Value;
            public int AccessCount;
        }
    }
}