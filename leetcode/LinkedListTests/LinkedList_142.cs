using LinkedList;

namespace LinkedListTests;

[TestFixture]
class LinkedList_142
{
    public static IReadOnlyList<ListNodeTestCase> LinkedListTestCases = new[]
    {
        new ListNodeTestCase(new []{ 3, 2, 0, -4 }, 1),
        new ListNodeTestCase(new []{ 1, 2}, 0),
        new ListNodeTestCase(new []{ 1}, -1)
    };

    [TestCaseSource(nameof(LinkedListTestCases))]
    public void TestDetectCycle(ListNodeTestCase testCase)
    {
        var solution = new Solution();
        var actual = solution.DetectCycle(testCase.Head);
        Assert.That(actual, Is.EqualTo(testCase.CycleNode));
    }

    private class Solution
    {
        public ListNode? DetectCycle(ListNode? head)
        {
            var slow = head;
            var fast = head;
            while (fast is not null && fast.next is not null)
            {
                fast = fast.next.next;
                slow = slow!.next;
                if (slow == fast) break;
            }

            if (fast == null || fast.next == null) return null;
            slow = head;
            while (slow != fast)
            {
                slow = slow!.next;
                fast = fast!.next;
            }

            return slow;
        }
    }

    public class ListNodeTestCase
    {
        public ListNode? Head;
        public ListNode? CycleNode;

        public ListNodeTestCase(int[] data, int cycleIndex)
        {
            (Head, CycleNode) = ListNode.ConstructCycle(data, cycleIndex);
        }
    }
}