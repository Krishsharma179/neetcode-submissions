class Solution:
    def maxArea(self, heights: List[int]) -> int:

        first  = 0
        second = len(heights)-1
        output = 0
        length = 0
        width  = 0 

        while first < second:
            length = min(heights[first],heights[second])
            width =  second - first

            output = max(output, length * width)

            if heights[first]>heights[second]:
                second-=1
            else:
                first+=1

        return output             

            

            


        