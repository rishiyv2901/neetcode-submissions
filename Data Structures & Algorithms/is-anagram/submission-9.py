class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        s_map = {}
        t_map = {}

        for val in s:
            if s_map.get(val) == None:
                s_map[val] = 1
            else:
                s_map[val] = s_map[val] + 1

        for val in t:
            if t_map.get(val) == None:
                t_map[val] = 1
            else:
                t_map[val] = t_map[val] + 1

        if s_map == t_map:
            return True
        
        return False