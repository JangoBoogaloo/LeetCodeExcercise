namespace Array;

[TestFixture]
internal class Array_706
{
    private class MyHashMap {
        int[] map;

        public MyHashMap() {
            map = new int[1000001];    
        }
    
        public void Put(int key, int value) {
            map[key] = value + 1;
        }
    
        public int Get(int key) {
            return map[key] -1;
        }
    
        public void Remove(int key) {
            map[key] = 0;
        }
    }
}