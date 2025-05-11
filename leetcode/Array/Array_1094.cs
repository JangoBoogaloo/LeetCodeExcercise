namespace Array;

[TestFixture]
class Array_1094
{
    class SortedDictionarySolution {
        public bool CarPooling(int[][] trips, int capacity) {
            var locationPassengerDiffMap = new SortedDictionary<int, int>();
            foreach(var trip in trips)
            {
                locationPassengerDiffMap[trip[1]] = locationPassengerDiffMap.GetValueOrDefault(trip[1],0) + trip[0];
                locationPassengerDiffMap[trip[2]] = locationPassengerDiffMap.GetValueOrDefault(trip[2],0) - trip[0];
            }

            var used = 0;

            foreach (var change in locationPassengerDiffMap.Values)
            {
                used += change;
                if (used > capacity)
                {
                    return false;
                }
            }
            return true;
        }
    }

    class BucketSolution
    {
        public bool CarPooling(int[][] trips, int capacity) {
            var diffs = new int[1001];
            var results = new int[diffs.Length];
            foreach(var trip in trips) {
                diffs[trip[1]] += trip[0];
                var destination = trip[2];
                if(destination < diffs.Length) {
                    diffs[destination] -= trip[0];
                }
            }
            results[0] = diffs[0];
            if(results[0] > capacity) return false;
            for(var i=1; i<diffs.Length; i++) {
                results[i] = results[i-1] + diffs[i];
                if(results[i] > capacity) return false;
            }
            return true;
        }
    }
}
