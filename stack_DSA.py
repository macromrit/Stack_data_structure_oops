class Stack:
    #constructor
    def __init__(self, *pre_elems, max_len) -> None:
        self.max = max_len
        self.min = 0
        self.object = list()
        self.object.extend(pre_elems)
    
    def push(self, element):
        if len(self.object)<self.max:
            self.object.append(element)
        else:
            print('Stack|- Over Flow Error')
    
    def pop(self):
        try: self.object.pop()
        except IndexError: print('Under Flow Error')
        
    def display(self):
        return self.object
    
    def __str__(self):
        return 'Stack created successfully| memory -> {}'.format(id(self))
    
    #destructor
    def __del__(self):
        print('Stack Destroyed | memory -> {}'.format(id(self)))
    
if __name__=='__main__': 
    #hit on what ya want -->
    pass
    
        
    
        