class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        res = ""
        carry = 0
        a, b = a[::-1], b[::-1]
        for i in range(max(len(a), len(b))):
            digitA = int(a[i]) if i < len(a) else 0
            digitB = int(b[i]) if i < len(b) else 0

            total = digitA + digitB + carry
            char = str(total%2)
            res = char + res
            carry = total//2
        if carry:
            res = "1" + res
        return res
    

        # More efficient n space (not quadratic)
        res = [""]
        carry = 0
        a, b = a[::-1], b[::-1]
        for i in range(max(len(a), len(b))):
            digitA = int(a[i]) if i < len(a) else 0
            digitB = int(b[i]) if i < len(b) else 0

            total = digitA + digitB + carry
            char = str(total%2)
            res.append(char)
            carry = total//2
        if carry:
            res.append("1")
        res.reverse()
        return "".join(res)