using System.Text;

namespace LinkedListTests;

internal class TextEditor
{
    private Stack<char> _left;
    private Stack<char> _right;
    
    public TextEditor()
    {
        _left = new Stack<char>();
        _right = new Stack<char>();
    }

    public void AddText(string text) {
        foreach (var ch in text)
        {
            _left.Push(ch);
        }
    }
    
    public int DeleteText(int k)
    {
        var actualDelete = 0;
        while (_left.Any() && k > 0)
        {
            _left.Pop();
            actualDelete++;
            k--;
        }

        return actualDelete;
    }
    
    public string CursorLeft(int k)
    {
        while (_left.Any() && k > 0)
        {
            var c = _left.Pop();
            _right.Push(c);
            k--;
        }
        return Get10LeftString();
    }
    
    public string CursorRight(int k)
    {
        while (_right.Any() && k > 0)
        {
            var c = _right.Pop();
            _left.Push(c);
            k--;
        }

        return Get10LeftString();
    }

    private string Get10LeftString()
    {
        var strB = new List<char>();
        var leftCount = 10;
        while (_left.Any() && leftCount > 0)
        {
            var c = _left.Pop();
            strB.Add(c);
            leftCount--;
        }
        strB.Reverse();
        foreach(var c in strB)
        {
            _left.Push(c);
        }
        return new string(strB.ToArray());
    }
}