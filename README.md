# Python-Arpeggiator

This class was written using music21 Python Library (beforehand you should install it and setup the openining .xml files), as well as with standart modules random and itertools.

The code creates arpeggiated chords, and makes it possible for number of voices. Also there is a function to enable cross-rhythms. The demo wav file below demostrates the example given in the code file. 

This is the first version of the program, some possible debugging changes are considered. 

To make the variant of your arpeggio set, type in blank .py file in the directory of the "arpeggiator.py" and run the script:


=================================================================

from arpeggiator import Arpeggiator

set = Arpeggiator([i,i,....,i,], x, y, "ratio:ratio")

set.process('half', 'midi')

=================================================================

*where i are the pc-sets on the notes, x - the number of patterns needed, y - the number of voices, ratio - the number of th ratio, for example "3:4"
*'midi' parameter is optional, by default it shoud be opened in you music program like MuseScore or Finale in notation

