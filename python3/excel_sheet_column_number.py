class Solution:
    def titleToNumber(self, s: str) -> int:
        result = 0
        letter_to_num_map = {
            'A': 1,
            'B': 2,
            'C': 3,
            'D': 4,
            'E': 5,
            'F': 6,
            'G': 7,
            'H': 8,
            'I': 9,
            'J': 10,
            'K': 11,
            'L': 12,
            'M': 13,
            'N': 14,
            'O': 15,
            'P': 16,
            'Q': 17,
            'R': 18,
            'S': 19,
            'T': 20,
            'U': 21,
            'V': 22,
            'W': 23,
            'X': 24,
            'Y': 25,
            'Z': 26
        }

        for i in range(len(s)):
            result += letter_to_num_map[s[len(s)-i-1]]*(26**i)

        return result


def main():
    s = Solution()
    actual_result = s.titleToNumber("ZY")
    print("Expected result is: 701, actual result is: " + str(actual_result))


if __name__ == "__main__":
    main()