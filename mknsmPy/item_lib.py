class Lib:
    
    lib = []

    def __init__(self,lib=lib):
        
        self.lib = lib
    
    def head(self, l=5):
       
        self.head = self.lib[:l]
        return self.head
        
    def tail(self, l=5):

        tail_len = int(len(self.lib)) - l
        self.tail = self.lib[tail_len:]
        return self.tail

    def set(self, s=0, e=-1):

        self.set = self.lib[s:e]
        return self.set
