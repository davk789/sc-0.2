'''
Created on Aug 15, 2011

Try to implement Tdef. It would be nice to recreate the functionality of sc's
pattern classes in their entirety. Someday, maybe. But for now, implement Tdef
and fork().

@author: davk
'''

import threading

def fork():
    """exposing a simplified threading interface to match sc"""
    return None

class Tdef(threading.Thread):
    def __init__(self, key, func=None):
        threading.Thread.__init__(self)
        if func:
            setattr(Tdef, key, func)
            return Tdef # let's pretend this is a classmethod
        
        
    
    def run(self):
        pass
    
    @classmethod
    def play(cls, key):
        print key, cls.tasks
    

def test():
    pass

if __name__ == "__main__":
    test()
