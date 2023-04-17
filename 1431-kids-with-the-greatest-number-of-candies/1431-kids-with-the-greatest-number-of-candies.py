class Solution:
    def kidsWithCandies(self, candies: List[int], e: int) -> List[bool]:
        max_val = max(candies)
        new_arr = []
        for val in candies:
            if val+e>=max_val:
                new_arr.append(True)
            else:
                new_arr.append(False)
        return new_arr