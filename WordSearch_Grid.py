class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        
        i=0
        while i<len(board):
            j=0
            while j<len(board[0]):
                # look for the starting letter in the grid and if it exists call recursive backtracking call to see if the adjacent letters are present 
                if (board[i][j]==word[0]) and (self.adj_exist(board,i,j,0,word) ):
                    return True
                j+=1
            i+=1
        return False
            
    def adj_exist(self,board, i, j, pos,word):
        # check if word length exceeds
        if pos==len(word):
            return True
        # check for borders
        if (i>=len(board)) or (j>=len(board[0])) or (i<0) or (j<0):
            return False
        if board[i][j]!=word[pos]:
            return False
        
        # temp variable to backtrack
        temp=board[i][j]
        # to mark visited letter
        board[i][j]='#'
    
        if (self.adj_exist(board,i+1,j,pos+1,word))or(self.adj_exist(board,i,j+1,pos+1,word))or(self.adj_exist(board,i-1,j,pos+1,word))or(self.adj_exist(board,i,j-1,pos+1,word)):
            return True
        board[i][j]=temp
