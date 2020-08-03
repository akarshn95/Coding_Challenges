class TrieNode(object):
    def __init__(self):
        self.isWord = False
        self.children = collections.defaultdict(TrieNode)

class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        currNode = self.root
        
        for char in word:
            currNode = currNode.children[char]
            
        currNode.isWord =  True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        currNode = self.root
        
        for char in word:
            if not char in currNode.children:
                return False
            currNode = currNode.children[char]
            
        return currNode.isWord

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        currNode = self.root
        
        for char in prefix:
            if not char in currNode.children:
                return False
            currNode = currNode.children[char]
            
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
