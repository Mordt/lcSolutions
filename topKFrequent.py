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
                
        print(freq)

