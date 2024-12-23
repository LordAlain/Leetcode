class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []

        # Sort intervals by the start time
        intervals.sort(key=lambda x: x[0])

        # Initialize the result list with the first interval
        result = [intervals[0]]

        for i in range(1, len(intervals)):
            current_interval = result[-1]
            next_interval = intervals[i]

            # If the current interval overlaps with the next interval, merge them
            if current_interval[1] >= next_interval[0]:
                current_interval[1] = max(current_interval[1], next_interval[1])
            else:
                # Otherwise, add the next interval to the result
                result.append(next_interval)

        return result