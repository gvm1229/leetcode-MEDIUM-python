class Solution:
    def intToRoman(self, num: int) -> str:
        toReturn = ""

        for i in range(len(str(num))-1, -1, -1):
            # i = number of 0s (digits-1) in a number
            placeValue = num // 10 ** i

            if i == 3:      # 1000s
                toReturn += "M" * placeValue
            elif i == 2:    # 100s
                toReturn += "C" * placeValue
            elif i == 1:    # 10s
                toReturn += "X" * placeValue
            elif i == 0:    # 1s
                toReturn += "I" * placeValue

            if placeValue != 0: num %= 10 ** i

        toReturn = toReturn.replace("IIIIIIIII", "IX")  # 9
        toReturn = toReturn.replace("IIIII", "V")       # 5
        toReturn = toReturn.replace("IIII", "IV")       # 4
        toReturn = toReturn.replace("XXXXXXXXX", "XC")  # 90
        toReturn = toReturn.replace("XXXXX", "L")       # 50
        toReturn = toReturn.replace("XXXX", "XL")       # 40
        toReturn = toReturn.replace("CCCCCCCCC", "CM")  # 900
        toReturn = toReturn.replace("CCCCC", "D")       # 500
        toReturn = toReturn.replace("CCCC", "CD")       # 400

        return toReturn


p1 = Solution()
# Constraints: 1 <= num <= 3999
print(p1.intToRoman(3))         # Expected output: III
print(p1.intToRoman(58))        # Expected output: LVIII
print(p1.intToRoman(1994))      # Expected output: MCMXCIV