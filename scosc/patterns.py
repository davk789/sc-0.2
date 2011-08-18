'''
Created on Aug 15, 2011

Try to implement Tdef. It would be nice to recreate the functionality of sc's
pattern classes in their entirety. Someday, maybe. But for now, implement Tdef
and fork().

@author: davk
'''

import threading
import Queue

import time

def fork(func):
    """
    essentially just an alias for calling a function in a thread.
    """
    return threading.Thread(target=func).start()

def wait(time):
    time.sleep(time)


class Task(threading.Thread):
    """
    implement the salient features from SC's task here.
    """
    def __init__(self, func):
        threading.Thread.__init__(self)
        self.function = func
        
    def run(self):
        return self.function()

    def play(self):
        return self.start()

    def stop(self):
        pass

    def reset(self):
        pass

def test():
    import sys
    def tester():
        for i in range(4):
            print "blabla", i
            time.sleep(0.2)
        return 1234
    
    tasck = Task(tester)
    tasck.play()
    sys.exit(0)


if __name__ == "__main__":
    test()
