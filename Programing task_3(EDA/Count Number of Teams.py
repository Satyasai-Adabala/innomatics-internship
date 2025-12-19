from typing import List

class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        result = 0
        
        for j in range(n):
            left_smaller = left_greater = right_smaller = right_greater = 0
            
            # Count left side
            for i in range(j):
                if rating[i] < rating[j]:
                    left_smaller += 1
                else:
                    left_greater += 1
            
            # Count right side
            for k in range(j+1, n):
                if rating[k] > rating[j]:
                    right_greater += 1
                else:
                    right_smaller += 1
            
            # Add valid teams
            result += left_smaller * right_greater
            result += left_greater * right_smaller
        
        return result
