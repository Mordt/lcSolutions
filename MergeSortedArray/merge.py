class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        print(len(nums1))
        for i in range(-1,n):
            print(-i, nums1[-i])
            if nums1[-i] == 0:
                nums1.pop(-i)
        
        for x in nums2:
            nums1.insert(0, x)
                
        nums1.sort()

