
class Solution:
    def reverse(self, x: int) -> int:
        if ( x >= 2**31 or x < -2**31 ):
            return 0
        else: 
            sign = -1 if x < 0 else 1
            x *= sign
            ans = 0

            while x:
                ans = ans*10 + (x%10)
                x //= 10

            ans *= sign
            return ans


if __name__ == '__main__':
    input_x = 123
    
    solution = Solution()
    output = solution.reverse(input_x)
    print("Output: ", output)
