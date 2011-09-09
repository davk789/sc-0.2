'''
Created on Aug 15, 2011

Jamming any SC-esque control structures here. Maybe something will stick.

@author: davk
'''

import random
import copy

class Pattern(object):
    """Base class for Pattern objects. These classes are here as a convenience, 
    and do not attempt to replicate SC's pattern classes exactly.
    
    Intended use:
    p = Pseq([2,3,4,5,6])
    print p.next()
    print p.next()
    print p.next()
    """
    def __init__(self, list, iter=None):
        self.sequence = list
        if iter:
            self.maxcount = len(list) * iter
        else:
            self.maxcount = None 
        self.counter = 0
    
    def next(self):
        """Subclasses must implement a next() method."""
        index = self.next_index()
        
        if self.maxcount is None or self.counter < self.maxcount:
            return self.do_next(index)
        else:
            return None

    def do_next(self):
        print "Subclass must implement Pattern.do_next()!"
        
    def next_index(self):
        index = self.counter % len(self.sequence)
        self.counter += 1
        return index

    def reset(self):
        """Subclasses need to implement a reset() method."""
        self.counter = 0

class Pseq(Pattern):
    def __init__(self, list, repeats=None):
        super(Pseq, self).__init__(list, repeats)
        
    def do_next(self, index):
        return self.sequence[index]

class Pshuf(Pattern):
    def __init__(self, list, repeats=None):
        super(Pshuf, self).__init__(list, repeats)

    def do_next(self, index):
        if index == 0:
            random.shuffle(self.sequence)
        return self.sequence[index]
# ... More classes to follow

def test():
    list = [random.random() * float(i) for i in range(10)]
    print list
    seq = Pshuf(list)
    for i in range(25):
        print seq.next()


if __name__ == "__main__":
    test()
