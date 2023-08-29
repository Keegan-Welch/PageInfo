from pyo import *
s = Server().boot()
s.amp = 1
a = Sine().out()   # Plays on left channel
a2 = Sine().out(1) # Plays on right channel
s.gui(locals())