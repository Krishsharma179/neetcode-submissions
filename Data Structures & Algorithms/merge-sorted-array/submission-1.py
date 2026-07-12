class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # so we will use two pointer but first pointer will be on the first nums 
        # second pointer will be on the second nums 

        first=0
        second=0
        
        while first<len(nums1) and second<len(nums2):
            if first>=m:
                nums1[first]=nums2[second]
                first+=1
                second+=1
            else:
                first+=1   

        nums1.sort()         
        


