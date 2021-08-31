
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        _max = 0
        _set = set()
        
        for i in range(len(s)):
            if (i + _max) > len(s):
                break
                
            _set = set(s[i:i+_max])
            if _max == len(_set): 
                for c in s[i+_max:]:
                    if c not in _set:
                        _set.add(c)
                        _max += 1
                    else:
                        break
        
        
        return _max

if __name__ == '__main__':
    s = "abcabcbb"
    
    solution = Solution()
    output = solution.lengthOfLongestSubstring(s)
    print("Output: ", output)
    
