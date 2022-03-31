class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        for x in nums2:
            nums1.insert(0, x)
            
        #while 0 in nums1:
        #    nums1.remove(0)
            
        for i in range(m,m+n):
            if nums1[i] == 0:
                nums1.del(i)
                
        nums1.sort()



