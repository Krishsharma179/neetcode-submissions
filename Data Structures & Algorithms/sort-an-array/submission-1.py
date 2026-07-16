class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        # First divied the array 
        def merge(arr, L , M , R ):

            arr1 , arr2 = arr[L:M+1],arr[M+1:R+1]
            
            i,j,k = L,0,0

            while j < len(arr1) and k < len(arr2):

                if arr1[j] <= arr2[k]:
                    arr[i]=arr1[j]
                    j+=1
                else:
                    arr[i] = arr2[k]
                    k+=1

                i+=1

            while j < len(arr1):
                nums[i]=arr1[j]

                j+=1
                i+=1

            while  k < len(arr2):

                nums[i]=arr2[k]

                k+=1
                i+=1


         

        def mergesort(arr , l , r):

            if l==r:
                return arr

            m = (l+r)// 2 

            mergesort(arr,l,m)
            mergesort(arr,m+1,r)
            merge(arr,l,m,r)
       
        
        mergesort(nums , 0, len(nums)-1)       

        return nums    








                
        