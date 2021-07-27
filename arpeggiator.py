from itertools import permutations
from music21.serial import ToneRow
from music21 import stream, note, duration, meter
from random import choice


class Arpeggiator:

    def __init__(self, input_notes, num_of_patterns, voices, ratio):
        self.x_patterns = num_of_patterns
        self.y_voices = voices
        self.req = len(input_notes)
        self.container = self.__prepare_notes(input_notes)
        self.chce = []
        self.__make_choice()

        try:
            self.time_ratio = list(map(int, ratio.split(":")))
            if len(self.time_ratio) < self.y_voices:
                for _ in range(self.y_voices - len(self.time_ratio)):
                    self.time_ratio.append(4)
            else:
                self.time_ratio.append(4)
        except ValueError:
            self.time_ratio = []
            for _ in range(self.y_voices):
                self.time_ratio.append(4)

    @staticmethod
    def __prepare_notes(input_notes):
        req = ToneRow(input_notes).noteNames()
        combinations = list(permutations(req))
        return combinations

    def __make_choice(self):
        for _ in range(self.x_patterns):
            measure = []
            for _ in range(self.y_voices):
                measure.append(choice(self.container))
            self.chce.append(measure)

    def __adjust_with_ratio(self):
        notes_total = self.x_patterns * self.req  # by max versus value
        note_counter = []
        for rate in self.time_ratio:
            note_counter.append(notes_total // max(self.time_ratio) * rate)

        chce = []
        for i in range(self.x_patterns):  # will count by max versus value
            measure = []
            for j in range(self.y_voices):
                if note_counter[j] <= 0:
                    measure.append(choice(self.container)[:0])
                else:
                    measure.append(choice(self.container)[:int(note_counter[j])])
                    note_counter[j] -= self.req
            chce.append(measure)

        return chce

    def process(self, duration_type, file_type=None):
        chce = self.__adjust_with_ratio()

        sc = stream.Score()

        for i in range(self.y_voices):
            part = stream.Part()
            if duration_type == 'half':
                part.append(meter.TimeSignature('4/2'))
            part.id = 'part%s' % i
            for note_seq in chce:

                for nstr in range(len(note_seq[i])):
                    time = duration.Tuplet(self.time_ratio[i],
                                           self.time_ratio[-1])
                    time.setDurationType(duration_type)
                    length = duration.Duration(duration_type)
                    length.appendTuplet(time)
                    n = note.Note(note_seq[i][nstr])
                    n.duration = length

                    part.append(n)
            sc.insert(0, part)
        sc.show(file_type)


n = Arpeggiator([0, 2, 4, 5, 7, 9, 11], 19, 4, "17:13:19:11")  # example
n.process('half','midi')                                # might be quarter, 16th or eighth, filetype can be "midi" or None by default                              # might be quarter, 16th or eighth, filetype can be "midi" or None by default
