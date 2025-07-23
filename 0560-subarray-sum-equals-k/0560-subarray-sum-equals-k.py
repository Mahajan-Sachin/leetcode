class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        track = {0: 1}  # prefix_sum count dictionary
        curr = 0
        result = 0

        for num in nums:
            curr += num

            if (curr - k) in track:
                result += track[curr - k]  # ✅ add number of times (curr - k) has appeared

            track[curr] = track.get(curr, 0) + 1  # ✅ always update count of current prefix sum

        return result
