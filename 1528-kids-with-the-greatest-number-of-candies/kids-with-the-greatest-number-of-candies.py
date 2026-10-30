class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        maxi_candy=max(candies)
        res=[]
        for candy in candies:
            if (candy+extraCandies)>=maxi_candy:
                res.append(True)
            else:
                    res.append(False)
        return res