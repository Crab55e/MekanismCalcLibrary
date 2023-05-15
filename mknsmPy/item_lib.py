class Lib:
    
    lib = []

    def show(self):
        return self.lib
    
    def head(self, length = 5):
        return self.lib[:length] 
    
    def tail(self, length = 5):
        return self.lib[(int(len(self.lib)) - length):]
    
    def set(self, start, end):
        return self.lib[start:end]
