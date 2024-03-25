namespace TwoPointersTests;

[TestFixture]
internal class TwoPointers_253
{
    class SolutionPQ {
        public int MinMeetingRooms(int[][] intervals)
        {
            Array.Sort(intervals, (x,y) => x[0] - y[0]);
            var priorityQueue = new PriorityQueue<int, int>();
            priorityQueue.Enqueue(intervals[0][1], intervals[0][1]);
            for (var i = 1; i < intervals.Length; i++)
            {
                var meetingEndTime = priorityQueue.Peek();
                //whenever we request a room, we check if we can release a room, if we can't we create a new room (increase the PQ size)
                if (meetingEndTime <= intervals[i][0])
                {
                    priorityQueue.Dequeue();
                }
                priorityQueue.Enqueue(intervals[i][1],intervals[i][1]);
            }

            return priorityQueue.Count;
        }
    }

    class SolutionTwoPointers
    {
        public int MinMeetingRooms(int[][] intervals)
        {
            var startTimes = intervals.Select(i => i[0]).ToArray();
            var endTimes = intervals.Select(i => i[1]).ToArray();
        
            Array.Sort(startTimes);
            Array.Sort(endTimes);
            var usedRooms = 0;
            var startTimePointer = 0;
            var endTimePointer = 0;
            while (startTimePointer < startTimes.Length)
            {
                if (startTimes[startTimePointer] >= endTimes[endTimePointer])
                {
                    endTimePointer++;
                }
                else
                {
                    usedRooms++;
                }
                startTimePointer++;
            }
            return usedRooms;
        }
    }
}
