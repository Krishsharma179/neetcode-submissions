class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # first check if all the rows has non duplicate element 
        
        output = True 

        for row in board:
            count={}
            for j in row:
                if j not in count and j != ".":
                    count[j]=1
                elif j in count and j != ".":
                    count[j]+=1    

            for key,val in count.items():
                if val > 1:
                    return False
                    

        # Now we will check if all the cloumns has non duplicate element

        for i in range(9):
            count = set()
            for row in board:                
                if row[i] == ".":
                    continue
                if row[i]  in count:
                    return False
                count.add(row[i])

                     

             
        print("col ok")
        #  now check for every 3*3 box

        for square in range(9):
            seen = set()
            for i in range(3):
                for j in range(3):
                    row = (square//3) * 3 + i
                    col = (square % 3) * 3 + j
                    if board[row][col] == ".":
                        continue
                    if board[row][col] in seen:
                        return False
                    seen.add(board[row][col])


        return output          



        
        