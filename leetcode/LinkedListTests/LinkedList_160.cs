
namespace LinkedListTests;

[TestFixture]
class LinkedList_160
{
    private class SolutionHash
    {
        public ListNode GetIntersectionNode(ListNode headA, ListNode headB)
        {
            var nodesInA = new HashSet<ListNode>();
            var tempA = headA;
            while (tempA is not null)
            {
                nodesInA.Add(tempA);
                tempA = tempA.next;
            }
            while (headB is not null)
            {
                if (nodesInA.Contains(headB)) return headB;
                headB = headB.next;
            }

            return null;
        }
    }

    private class SolutionTwoPointers
    {
        public ListNode GetIntersectionNode(ListNode headA, ListNode headB)
        {
            var tailA = GetLast(headA);
            tailA.next = headA;
            var intersect = DetectCycle(headB);
            tailA.next = null;
            return intersect;
            ListNode? GetLast(ListNode? head)
            {
                if (head is null) return null;
                while (head is not null)
                {
                    if (head.next is null) return head;
                    head = head.next;
                }
                return null;
            }
            
            ListNode? DetectCycle(ListNode? head)
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
    }

    public static IReadOnlyList<LinkedList_160TestCase> LinkedListTestCases = new[]
    {
        new LinkedList_160TestCase(
            new []{ 4,1 }, 
            new []{ 5,6,1 }, 
            new []{8,4,5}),
        new LinkedList_160TestCase(
            new []{ 1, 9, 1}, 
            new []{ 3 }, 
            new []{ 2, 4 }),
        new LinkedList_160TestCase(
            new []{ 2, 6, 4}, 
            new []{ 1,5 }, 
            Array.Empty<int>()),
    };

    [TestCaseSource(nameof(LinkedListTestCases))]
    public void TestLinkedList_160_Hash(LinkedList_160TestCase testCase)
    {
        var solution = new SolutionHash();
        var actual = solution.GetIntersectionNode(testCase.HeadA, testCase.headB);
        Assert.That(actual, Is.EqualTo(testCase.Intersect));
    }

    [TestCaseSource(nameof(LinkedListTestCases))]
    public void TestLinkedList_160_TwoPointers(LinkedList_160TestCase testCase)
    {
        var solution = new SolutionTwoPointers();
        var actual = solution.GetIntersectionNode(testCase.HeadA, testCase.headB);
        Assert.That(actual, Is.EqualTo(testCase.Intersect));
    }

    public class LinkedList_160TestCase
    {
        public ListNode? HeadA;
        public ListNode? headB;
        public ListNode? Intersect;

        public LinkedList_160TestCase(int[] aList, int[] bList, int[] intersect)
        {
            (HeadA, headB, Intersect) = ListNode.ConstructIntersectNodes(aList, bList, intersect);
        }
    }
}