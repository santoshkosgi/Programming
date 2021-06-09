class Solution:
    def canPlaceFlowers(self, flowerbed, n):
        for index, flower in enumerate(flowerbed):
            if n == 0:
                return True
            if index == 0 and flower == 0 and flowerbed[index+1] == 0:
                flowerbed[index] = 1
                n -= 1
                continue
            if index == len(flowerbed) - 1 and flowerbed[index-1] == 0:
                flowerbed[index] = 1
                n -= 1
                continue
            if flower == 0 and flowerbed[index-1] == 0 and flowerbed[index+1] == 0:
                flowerbed[index] = 1
                n -= 1
                continue
        if n == 0:
            return True
        return False

sol = Solution()
sol.canPlaceFlowers([1,0,0,0,1], 2)