class Note:
    def __init__(self, duration=0, pitch=60, volume=127):
        self.duration = duration
        self.pitch = pitch
        self.volume = volume

    def move(self, delta_pitch):
        self.pitch += delta_pitch


class Bar:
    def __init__(self, duration=16):
        self.duration = duration
        self.beats = tuple([] for i in range(self.duration))

    def add_notes(self, beat, *notes):
        for note in notes:
            self.beats[beat].append(note)

    def move(self, delta_pitch):
        for notes in self.beats:
            for note in notes:
                note.move(delta_pitch)


class Pattern:
    def __init__(self):
        self.bars = []

    def add_bar(self, bar):
        self.bars.append(bar)
