#Given a string s, remove duplicate letters so that every letter appears once and only once. 
#You must make sure your result is the smallest in lexicographical order among all possible results.


def removeDuplicateLetters(self, s: str) -> str:
        # reverse index dictionary
        ridx = {v:i for i,v in enumerate(s)}
        res = ''
        
        for i, val in enumerate(s):
            if val not in res:
                # add in lexicographical order
                while val < res[-1:] and i < ridx[res[-1:]]:
                    res = res[:-1]
                    
                res += val
                
        return res
