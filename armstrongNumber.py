class Solution:
    def armstrongNumber (self, n):
        digits = str(n)
        power = len(digits)
        arms_no = sum(int(d)**power for d in digits)
        return n == arms_no
