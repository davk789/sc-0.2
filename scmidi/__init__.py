"""
Implement SuperCollider-style midi responders in python. 

For now, this module depends on pygame. Maybe eventually I will try to wrap 
a python midi lib with boost and juce, but not for a while -- my main skill 
with C++ seems to be wallowing in confusion.
"""

__author__ = "davidkendall.net"
__license__ = "GNU Lesser General Public License"

from scmidi import *

