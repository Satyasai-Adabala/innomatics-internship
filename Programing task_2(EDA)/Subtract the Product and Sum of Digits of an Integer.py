class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product, summ = 1, 0
        for ch in str(n):
            digit = int(ch)
            product *= digit
            summ += digit
        return product - summ