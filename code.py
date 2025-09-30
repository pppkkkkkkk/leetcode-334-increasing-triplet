class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        min1 = float('inf')
        min2 = float('inf')
        for n in nums:
            print(n)
            print(min1)
            print(min2)
            print(' ')
            if n <= min1:
                min1 = n  # Update first minimum
            elif n <= min2:
                min2 = n  # Update second minimum
            else:
                return True  # Found a third number greater than both
        return False  # No triplet found