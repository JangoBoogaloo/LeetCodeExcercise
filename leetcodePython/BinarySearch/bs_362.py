import bisect


class HitCounter_Array:

    def __init__(self):
        self.hits = []

    def hit(self, timestamp: int) -> None:
        self.hits.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        start_time = max(0, timestamp - 300)
        print(start_time)
        # 0, 1 ,2 -> len = 3
        # 1 => 3 - 1 = 2
        return len(self.hits) - bisect.bisect_right(self.hits, start_time)


class HitCounter_300_Const:

    def __init__(self):
        self.hit_info = [(0, 0)] * 300

    def hit(self, timestamp: int) -> None:
        time_index = timestamp % 300
        prev_time, prev_hits = self.hit_info[time_index]
        # we are at another 300 cycle
        if prev_time != timestamp:
            self.hit_info[time_index] = timestamp, 1
        else:
            self.hit_info[time_index] = prev_time, prev_hits + 1

    def getHits(self, timestamp: int) -> int:
        ans = 0
        for i in range(0, len(self.hit_info)):
            time, hit = self.hit_info[i]
            if timestamp - time < 300:
                ans += hit
        return ans
