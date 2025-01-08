class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        length = len(temperatures)
        result = [0] * length
        
        # brute force using two pointers
        # for l, val in enumerate(temperatures):
        #     r = l + 1
        #     result[l] = 0
        #     while r < length:
        #         if val < temperatures[r]:
        #             result[l] = r - l
        #             break
        #         else:
        #             r += 1

        # dynamic programming using two pointers
        # We solve backwards
        for l in range(length - 2, -1, -1):
            r = l + 1
            while r < length and temperatures[r] <= temperatures[l]:
                # if the following value is 0, all remaining values are 0
                if result[r] == 0:
                    r = length
                    break
                # We can skip as we already calculated the distance to the next highest value
                r += result[r]
            
            if r < length:
                result[l] = r - l
        
        return result