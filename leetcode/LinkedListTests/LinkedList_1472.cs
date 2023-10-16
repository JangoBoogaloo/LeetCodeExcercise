namespace LinkedListTests;

[TestFixture]
class LinkedList_1472
{
    public class BrowserHistory {
        private DoubleNode history;

        public BrowserHistory(string homepage) {
            history = new DoubleNode(homepage);
        }
    
        public void Visit(string url) {
            history.next = new DoubleNode(url);
            history.next.prev = history;
            history = history.next;
        }
    
        public string Back(int steps) {
            while(history.prev is not null && steps >0) {
                history = history.prev;
                steps--;
            }
            return history.val;
        }
    
        public string Forward(int steps) {
            while(history.next is not null && steps >0) {
                history = history.next;
                steps--;
            }
            return history.val;
        }
    }
}