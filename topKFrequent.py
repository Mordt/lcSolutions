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
        tuples,
        key = lambda t: t[1]
        
        #return
        result = []
        for item in tuples:
            if k > 0:
                result.append(item[0])
                k -=1
            break
        
        print(result)
        return result


