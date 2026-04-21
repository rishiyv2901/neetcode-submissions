class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        track = {}

        for word in strs:
            key = ''.join(sorted(word))

            if key not in track:
                track[key] = []

            track[key].append(word)

        res = []

        for key in track:
            res.append(track[key])

        print(res)

        return res