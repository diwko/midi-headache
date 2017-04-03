from melody_parts import Note, Bar, Pattern
from random import randint


def generate_drum_bar(pitch, period, volume=127):
    bar = Bar()
    for i in range(0, 16, period):
        bar.add_notes(i, Note(1, pitch, volume))
    return bar


def generate_drum_pattern(bars_number, pitch, period, volume=127):
    pattern = Pattern()
    bar = generate_drum_bar(pitch, period, volume)
    for i in range(bars_number):
        pattern.add_bar(bar)
    return pattern


def generate_chord_notes(octave=5, chord_number=0, duration=1, volume=127):
    chord_basics = ((0, 4, 7), (2, 5, 9), (4, 7, 11),
                    (5, 9, 12), (7, 11, 15), (9, 12, 16))

    notes = []
    for basic_pitch in chord_basics[chord_number]:
        note = Note(duration, octave*12 + basic_pitch, volume)
        notes.append(note)
    return notes


def generate_chord_bar(octave=5, note_duration=1, volume=127):
    bar = Bar()
    chord = generate_chord_notes(octave, 0, note_duration, volume)
    for beat in range(0, 16, note_duration):
        if not randint(0, 3):
            continue
        if not randint(0, 1):
            chord = generate_chord_notes(octave, randint(0, 5),
                                         note_duration, volume)
        bar.add_notes(beat, *chord)
    return bar


def generate_chord_pattern(bars_number=4, octave=5, note_duration=1,
                           volume=127):
    pattern = Pattern()
    for bar in range(bars_number):
        pattern.add_bar(generate_chord_bar(octave, note_duration, volume))
    return pattern


def generate_notes(duration=16, octave=5, note_durations=(1, 2, 4, 8, 16),
                   note_chance=0.8, volume=127):
    note_basic = (0, 2, 4, 5, 7, 9, 11)
    notes = []
    beat = 0
    pitch = octave * 12
    while beat < duration:
        if randint(0, 100) > note_chance*100:
            beat += 1
            continue
        note_duration = note_durations[randint(0, len(note_durations) - 1)]
        if beat + note_duration < duration:
            if randint(0, 5) == 0:
                if not randint(0, 8):
                    pitch = octave*12
                else:
                    pitch = octave*12 + note_basic[
                        randint(0, len(note_basic)-1)]
            notes.append((beat, Note(note_duration, pitch, volume)))
        beat += note_duration
    return notes


def generate_bar(octave=5, note_durations=(1, 2, 4, 8, 16), note_chance=0.8,
                 volume=127):
    bar = Bar()
    notes = generate_notes(16, octave, note_durations, note_chance, volume)
    for note in notes:
        bar.add_notes(note[0], note[1])
    return bar


def generate_pattern(bars_number=1, octave=5, note_durations=(1, 2, 4, 8, 16),
                     note_chance=0.8, volume=127):
    pattern = Pattern()
    generated = generate_bar(octave, note_durations, note_chance, volume)
    bars = [generated]
    for bar in range(bars_number):
        if not randint(0, 1):
            generated = generate_bar(octave, note_durations,
                                     note_chance, volume)
            bars.append(generated)
        elif not randint(0, 1):
            generated = bars[randint(0, len(bars) - 1)]
        pattern.add_bar(generated)

    return pattern
