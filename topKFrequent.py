class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        #idea: create hashmap of number -> frequency
        #iterate through list, count every instance and add to map
        #at the end, grab the top k
        
        freq = {}
        
        for n in nums:
            if n not in freq:
                freq[n] = 1
            else:
                freq[n] += 1
        
        #turn dict into list of tuples
        tuples = []
        for key in freq:
            freqTuple = (key, freq[key])
            tuples.append(freqTuple)
        
        #sort tuples
        tuples = sorted(
            tuples,
            key = lambda t: t[1], 
            reverse = True
        )
        
        #return
        result = []
        for item in tuples:
            if k > 0:
                result.append(item[0])
                k -= 1
                continue
            break
        
        return result

#neetcode solution:
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for n, c in count.items():
            freq[c].append(n)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res

        # O(n)
