class Solution:
    import math
    def countPairs(self, deliciousness: List[int]) -> int:
        result = 0

        delicious_meals_list = [1, 2]
        for power in range(1, 22):
            delicious_meals_list.append(delicious_meals_list[-1] * 2)

        delicious_counter = {}
        for meal in deliciousness:
            delicious_counter[meal] = delicious_counter.get(meal, 0) + 1
        print(delicious_counter)
        for meal in delicious_counter:
            for power in delicious_meals_list:
                if power - meal in delicious_counter:
                    if meal == power - meal:
                        result += 2 * math.comb(delicious_counter[meal], 2)
                    else:
                        result += delicious_counter[meal] * delicious_counter[power - meal]

        return int(result / 2)

    def is_goodmean(self, delicious_meals_list, source, target):
        if (source + target) in delicious_meals_list:
            return True
        return False

sol = Solution()
print(sol.countPairs([]))