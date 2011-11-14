'''
Created on Oct 25, 2011

@author: davk

voicer.py

Voice manager for my own personal uses. This module holds base classes for 
typical sc stuff that I might do. Currently only consists of a PolySynth base
class, but should include MonoSynth DrumSynth and then eventually support 
inserts. Classic.

'''

from scosc import tools, controller



class PolySynth(object):
    """Base class for polyphonic synth manager. This class manages its own 
    voices by responding to midi style note and control methods.
    
    This class is to be used as a template to manage polyphonic synth control
    in scsynth. As such, to use the class requires adherence to certain 
    interface protocols.
    """
    def __init__(self, sdname=None):
        object.__init__(self)
        # initialize the data
        self.groupID = tools.nextNodeID()
        self.voices = {}
        self.params = {}
        self.name = sdname
        self.s = controller.Controller(("192.168.1.100", 57111))
        
        # run startup functions
        self.s.sendMsg('g_new', self.groupID, 1, 1)
    
    def __del__(self):
        self.s.sendMsg('n_free', self.groupID)
    
    # note section
    
    def note_on(self, note, args):
        """
        Do the note on. Pass relevant parameter settings as alternating key
        value arguments.
        """
        if note in self.voices:
            self.voices[note].append(tools.nextNodeID())
        else:
            self.voices[note] = [tools.nextNodeID()]
        
        for i in range(0, len(args), 2):
            self.params[args[i]] = args[i+1] 
                
        msg = (['s_new', self.name, self.voices[note][-1], 0, self.groupID] + 
         [val for pair in zip(self.params.keys(), self.params.values()) 
          for val in pair]) 
        self.s.listSendMsg(msg);

    def note_off(self, note, args):
        "note off and set relevant params. see self.note_on()"

        if len(self.voices[note]) > 0:
            voice = self.voices[note].pop()
        else:
            print "there's a problem with turning off voice", note
            return
    
        for i in range(0, len(args), 2):
            self.params[args[i]] = args[i+1] 

        self.s.listSendMsg(['n_set', voice, 'gate', 0] + 
                           [val for pair in zip(self.params.keys(), 
                                                self.params.values()) 
                            for val in pair])

    def mod(self, ctl, args):
        """same as note on/off -- use the controller number as the index, 
        provide the proper arguments."""

        for i in range(0, len(args), 2):
            self.params[args[i]] = args[i+1]
                    
        if ctl in self.voices:
            for voice in self.voices[ctl]:
                self.s.listSendMsg(['n_set', voice] +
                                   [val for pair in zip(self.params.keys(), 
                                                        self.params.values())
                                    for val in pair])
        else:
            print "I can't find the controller number" + str(ctl) + "!!!"
        
    # parameter section
    
    def set_param(self, key, val):
        "Set the stored parameter value and push to the synth server."
        self.params[key] = val
        self.s.sendMsg('n_set', self.groupID, key, self.params[key])
    
    def set_params(self, args):
        "take a list of alternating keys and values and set parameters."
        for i in range(0, len(args), 2):
            self.set_param(args[i], args[i+1])

        


if __name__ == "__main__":
    print "INSTALL THIS MODULE AND RUN TEST.PY"
    #test = PolySynth()
    #print repr(test)

