'''
Design a data structure that supports the following two operations:

void addWord(word)
bool search(word)
search(word) can search a literal word or a regular expression string containing only letters a-z or .. A . means it can represent any one letter.

Example:

addWord("bad")
addWord("dad")
addWord("mad")
search("pad") -> false
search("bad") -> true
search(".ad") -> true
search("b..") -> true

Note:
You may assume that all words are consist of lowercase letters a-z.

'''



# initialize a TrieNode class
class TrieNode(object):
    def __init__(self):
        self.isWord = False
        self.children = defaultdict(TrieNode)

class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: None
        """
        curr_node = self.root
        for char in word:
            curr_node = curr_node.children[char]

        curr_node.isWord = True                
        

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        # dfs to recursively search for char in case of '.'
        def dfs(node,i):
            # if i is length of word, we have reached end of word
            if i == len(word):
                return node.isWord
            
            if word[i]=='.':
                # search dfs for all children
                for child in node.children:
                    if dfs(node.children[child],i+1): 
                        return True
            
            if word[i] in node.children:
                return dfs(node.children[word[i]],i+1)
            
            return False
        return dfs(self.root,0)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
