class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []

        # Step 1: Sort intervals by start time
        intervals.sort()
        merged = [intervals[0]]

        # Step 2: Merge overlapping intervals
        for i in range(1, len(intervals)):
            if merged[-1][1] >= intervals[i][0]:
                # Merge
                merged[-1][1] = max(merged[-1][1], intervals[i][1])
            else:
                # No overlap → Add new interval
                merged.append(intervals[i])

        return merged
