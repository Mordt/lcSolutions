class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        
        #new idea:
        #have a pointer at each array, traverse 1 by 1 at n+m
        
        one, two = 0, 0
        for i in range(n+m):
            print(i, nums1[one], nums2[two])
            
            if nums1[one] >= nums2[two] or i == m:
                nums1.insert(i, nums2[two])
                one += 1
                two += 1
            else:#nums1[one] < nums2[two]
                #nums1.insert(i+1, nums2[two])#insert in current index
                one +=1
                #two +=1

        
