class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        warmest_temp = temperatures[-1]
        for day in range(len(temperatures) - 2, -1, -1):
            temp = temperatures[day]
            if temp >= warmest_temp:
                warmest_temp = temp
            else:
                next_day = day + 1
                while temperatures[next_day] <= temp:
                    next_day += answer[next_day]
                answer[day] = next_day - day
        return answer