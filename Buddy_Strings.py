"""
Given two strings A and B of lowercase letters, return true if you can swap two letters in A so the result is equal to B, otherwise, return false.

Swapping letters is defined as taking two indices i and j (0-indexed) such that i != j and swapping the characters at A[i] and A[j]. For example, swapping at indices 0 and 2 in "abcd" results in "cbad".
"""

def buddyStrings(self, A: str, B: str) -> bool:
        if set(list(A)) != set(list(B)) or len(A) != len(B):
            return False
        
        # if both strings are equal, they should have at least one repeating 
        # char to form buddy strings
        if A == B:
            return len(A) != len(set(A))
        else:
            idx = []
            for i in range(len(A)):
                if A[i] != B[i]:
                    idx.append(i)
            # make sure only 2 are swapped
            if len(idx) > 2:
                return False
            # make sure the swapping is proper
            return A[idx[0]] == B[idx[1]] and A[idx[1]] == B[idx[0]]
