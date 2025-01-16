class Trie:
    def __init__(self):
        # tree of nodes?
        # each node contains the set of nodes it directly point to
        # easier solution is have nested dictionaries
        # ie. {l:{e:{d:{.:.}}}}
        self.s_dict = {}

    def insert(self, word: str) -> None:
        # for every letter in the string
        # search if it exists, if not then create it
        # at the last letter, create a connection to NULL
        view = self.s_dict
        for l in word:
            if l not in view:
                view[l] = {}
            view = view[l]
        view["."] = "."

    def search(self, word: str) -> bool:
        # for every letter in the string
        # search if it exists, if not return False
        # at the last letter, verify it's a string ending
        # return True
        view = self.s_dict
        for l in word:
            if l not in view: return False
            view = view[l]
        if "." not in view: return False
        return True


    def startsWith(self, prefix: str) -> bool:
        # for every letter in the prefix
        # search if it exists, if not return False
        # return True
        view = self.s_dict
        for l in prefix:
            if l not in view: return False
            view = view[l]
        return True
        
# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)