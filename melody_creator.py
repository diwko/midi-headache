from midiutil import MIDIFile


class MelodyCreator:
    def __init__(self, path='melody.mid', tempo=200):
        self._path = path
        self._melody = MIDIFile(1, True, True, True)
        self._track = 0
        self._tempo = tempo
        self._melody.addTempo(self._track, 0, tempo)
        self._free_channels = [x for x in range(16, -1, -1) if x != 9]
        self._current_channel = 0
        self._beat_instrument = 0
        self._beat_drum = 0

    def add_instrument(self, instrument_number):
        self._current_channel = self._free_channels.pop()
        self._melody.addProgramChange(
            self._track, self._current_channel, 0, instrument_number)
        self._beat_instrument = 0

    def add_instrument_pattern(self, pattern):
        self._beat_instrument = self._add_pattern(
            self._current_channel, self._beat_instrument, pattern)

    def add_drum_pattern(self, pattern):
        self._beat_drum = self._add_pattern(9, self._beat_drum, pattern)

    def _add_pattern(self, channel, start_beat, pattern):
        for bar in pattern.bars:
            for notes in bar.beats:
                for note in notes:
                    self._add_note(channel, start_beat, note)
                start_beat += 1
        return start_beat

    def _add_note(self, channel, beat, note):
        self._melody.addNote(
            self._track, channel, note.pitch, beat, note.duration, note.volume)

    def save_melody(self):
        with open(self._path, "wb") as output_file:
            self._melody.writeFile(output_file)
