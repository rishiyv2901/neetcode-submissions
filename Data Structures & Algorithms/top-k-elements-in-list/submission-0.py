class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}

        for num in  nums:

            if num not in counter:
                counter[num] = 1
            else:
                counter[num] += 1

        print(counter)
        result = []

        while k>0:
            max_val = 0
            max_key = None
            for key in counter:
                if counter[key] > max_val:
                    max_val = counter[key]
                    max_key = key
            result.append(max_key)
            del counter[max_key]
            k -= 1

        print(result)

        return result
