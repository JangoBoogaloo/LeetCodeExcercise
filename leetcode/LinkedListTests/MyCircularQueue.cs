namespace LinkedListTests;
using System.Threading;

//https://leetcode.com/problems/design-circular-queue/description/
internal class MyCircularQueue
{
    private ListNode? _head, _tail;
    private int _count;
    private int _capacity;
    private readonly ReaderWriterLockSlim _readerWriterLock;

    public MyCircularQueue(int k)
    {
        _capacity = k;
        _count = 0;
        _readerWriterLock = new ReaderWriterLockSlim();
    }
    
    public bool EnQueue(int value)
    {
        _readerWriterLock.EnterWriteLock();
        var operationSuccess = false;
        if (_count < _capacity)
        {
            var newNode = new ListNode(value);
            if (_count > 0)
            {
                _tail!.next = newNode;
                _tail = newNode;
            }
            else
            {
                _head = _tail = newNode;
            }
            _count++;
            operationSuccess = true;
        }
        _readerWriterLock.ExitWriteLock();
        return operationSuccess;
        
    }
    
    public bool DeQueue()
    {
        _readerWriterLock.EnterWriteLock();
        var operationSuccess = false;
        if (_count > 0)
        {
            _head = _head!.next;
            _count--;
            operationSuccess = true;
        }
        _readerWriterLock.ExitWriteLock();
        return operationSuccess;
    }
    
    public int Front()
    {
        _readerWriterLock.EnterReadLock();
        var result = _count > 0 ? _head!.val : -1;
        _readerWriterLock.ExitReadLock();
        return result;
    }
    
    public int Rear() {
        _readerWriterLock.EnterReadLock();
        var result = _count > 0 ? _tail!.val : -1;
        _readerWriterLock.ExitReadLock();
        return result;
    }
    
    public bool IsEmpty()
    {
        _readerWriterLock.EnterReadLock();
        var result = _count == 0;
        _readerWriterLock.ExitReadLock();

        return result;
    }
    
    public bool IsFull()
    {
        _readerWriterLock.EnterReadLock();
        var result = _count == _capacity;
        _readerWriterLock.ExitReadLock();
        return result;
    }
}