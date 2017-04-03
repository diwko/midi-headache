from argparse import ArgumentParser, ArgumentTypeError, RawTextHelpFormatter
from random import randint


drums = {
    35: 'Acoustic Bass Drum',
    36: 'Bass Drum 1',
    37: 'Side Stick',
    38: 'Acoustic Snare',
    39: 'Hand Clap',
    40: 'Electric Snare',
    41: 'Low Floor Tom',
    42: 'Closed Hi Hat',
    43: 'High Floor Tom',
    44: 'Pedal Hi-Hat',
    45: 'Low Tom',
    46: 'Open Hi-Hat',
    47: 'Low-Mid Tom',
    48: 'Hi-Mid Tom',
    49: 'Crash Cymbal 1',
    50: 'High Tom',
    51: 'Ride Cymbal 1',
    52: 'Chinese Cymbal',
    53: 'Ride Bell',
    54: 'Tambourine',
    55: 'Splash Cymbal',
    56: 'Cowbell',
    57: 'Crash Cymbal 2',
    58: 'Vibraslap',
    59: 'Ride Cymbal 2',
    60: 'Hi Bongo',
    61: 'Low Bongo',
    62: 'Mute Hi Conga',
    63: 'Open Hi Conga',
    64: 'Low Conga',
    65: 'High Timbale',
    66: 'Low Timbale',
    67: 'High Agogo',
    68: 'Low Agogo',
    69: 'Cabasa',
    70: 'Maracas',
    71: 'Short Whistle',
    72: 'Long Whistle',
    73: 'Short Guiro',
    74: 'Long Guiro',
    75: 'Claves',
    76: 'Hi Wood Block',
    77: 'Low Wood Block',
    78: 'Mute Cuica',
    79: 'Open Cuica',
    80: 'Mute Triangle',
    81: 'Open Triangle'}

instruments = {
    0: 'Acoustic Grand Piano',
    1: 'Bright Acoustic Piano',
    2: 'Electric Grand Piano',
    3: 'Honky-tonk Piano',
    4: 'Electric Piano 1',
    5: 'Electric Piano 2',
    6: 'Harpsichord',
    7: 'Clavinet',
    8: 'Celesta',
    9: 'Glockenspiel',
    10: 'Music Box',
    11: 'Vibraphone',
    12: 'Marimba',
    13: 'Xylophone',
    14: 'Tubular Bells',
    15: 'Dulcimer',
    16: 'Drawbar Organ',
    17: 'Percussive Organ',
    18: 'Rock Organ',
    19: 'Church Organ',
    20: 'Reed Organ',
    21: 'Accordion',
    22: 'Harmonica',
    23: 'Tango Accordion',
    24: 'Acoustic Guitar (nylon)',
    25: 'Acoustic Guitar (steel)',
    26: 'Electric Guitar (jazz)',
    27: 'Electric Guitar (clean)',
    28: 'Electric Guitar (muted)',
    29: 'Overdriven Guitar',
    30: 'Distortion Guitar',
    31: 'Guitar Harmonics',
    32: 'Acoustic Bass',
    33: 'Electric Bass (finger)',
    34: 'Electric Bass (pick)',
    35: 'Fretless Bass',
    36: 'Slap Bass 1',
    37: 'Slap Bass 2',
    38: 'Synth Bass 1',
    39: 'Synth Bass 2',
    40: 'Violin',
    41: 'Viola',
    42: 'Cello',
    43: 'Contrabass',
    44: 'Tremolo Strings',
    45: 'Pizzicato Strings',
    46: 'Orchestral Harp',
    47: 'Timpani',
    48: 'String Ensemble 1',
    49: 'String Ensemble 2',
    50: 'Synth Strings 1',
    51: 'Synth Strings 2',
    52: 'Choir Aahs',
    53: 'Voice Oohs',
    54: 'Synth Choir',
    55: 'Orchestra Hit',
    56: 'Trumpet',
    57: 'Trombone',
    58: 'Tuba',
    59: 'Muted Trumpet',
    60: 'French Horn',
    61: 'Brass Section',
    62: 'Synth Brass 1',
    63: 'Synth Brass 2',
    64: 'Soprano Sax',
    65: 'Alto Sax',
    66: 'Tenor Sax',
    67: 'Baritone Sax',
    68: 'Oboe',
    69: 'English Horn',
    70: 'Bassoon',
    71: 'Clarinet',
    72: 'Piccolo',
    73: 'Flute',
    74: 'Recorder',
    75: 'Pan Flute',
    76: 'Blown bottle',
    77: 'Shakuhachi',
    78: 'Whistle',
    79: 'Ocarina',
    80: 'Lead 1 (square)',
    81: 'Lead 2 (sawtooth)',
    82: 'Lead 3 (calliope)',
    83: 'Lead 4 (chiff)',
    84: 'Lead 5 (charang)',
    85: 'Lead 6 (voice)',
    86: 'Lead 7 (fifths)',
    87: 'Lead 8 (bass + lead)',
    88: 'Pad 1 (new age)',
    89: 'Pad 2 (warm)',
    90: 'Pad 3 (polysynth)',
    91: 'Pad 4 (choir)',
    92: 'Pad 5 (bowed)',
    93: 'Pad 6 (metallic)',
    94: 'Pad 7 (halo)',
    95: 'Pad 8 (sweep)',
    96: 'FX 1 (rain)',
    97: 'FX 2 (soundtrack)',
    98: 'FX 3 (crystal)',
    99: 'FX 4 (atmosphere)',
    100: 'FX 5 (brightness)',
    101: 'FX 6 (goblins)',
    102: 'FX 7 (echoes)',
    103: 'FX 8 (sci-fi)',
    104: 'Sitar',
    105: 'Banjo',
    106: 'Shamisen',
    107: 'Koto',
    108: 'Kalimba',
    109: 'Bagpipe',
    110: 'Fiddle',
    111: 'Shanai',
    112: 'Tinkle Bell',
    113: 'Agogo',
    114: 'Steel Drums',
    115: 'Woodblock',
    116: 'Taiko Drum',
    117: 'Melodic Tom',
    118: 'Synth Drum',
    119: 'Reverse Cymbal',
    120: 'Guitar Fret Noise',
    121: 'Breath Noise',
    122: 'Seashore',
    123: 'Bird Tweet',
    124: 'Telephone Ring',
    125: 'Helicopter',
    126: 'Applause',
    127: 'Gunshot128'}

instrument_categories = (
    'Piano',
    'Chromatic Percussion',
    'Organ',
    'Guitar',
    'Bass',
    'Strings',
    'Ensemble',
    'Brass',
    'Reed',
    'Pipe',
    'Synth Lead',
    'Synth Pad',
    'Synth Effects',
    'Ethnic',
    'Percussive',
    'Sound effects')

not_mapped_instruments = {3, 10, 11, 12, 17, 18, 20, 22, 31, 39,
                          41, 43, 49, 50, 51, 52, 54, 55, 62, 63,
                          77, 78, 81, 82, 83, 85, 86, 87, 89, 90,
                          91, 92, 93, 96, 97, 99, 100, 103, 105, 106,
                          107, 108, 109, 110, 111, 112, 113, 116, 117, 118,
                          119, 121, 123, 124, 126, 127}


def file_type(string):
    if not str.endswith(string, '.midi'):
        string += '.midi'
    return string


def tempo_type(string):
    tempo = int(string)
    if tempo < 50 or tempo > 500:
        raise ArgumentTypeError("Tempo has to be between 50 and 500")
    return tempo


def bars_type(string):
    bars = int(string)
    if bars < 1:
        raise ArgumentTypeError("Bars has to be greater than 0")
    return bars


def drum_type(string):
    drum = int(string)
    if drum < 35 or drum > 81:
        raise ArgumentTypeError("Drum has to be between 35 and 81")
    return drum


def instrument_type(string):
    instrument = int(string)
    if instrument < 0 or instrument > 125:
        raise ArgumentTypeError("Instrument has to be between 0 and 125")

    mapped = True
    while instrument in not_mapped_instruments:
        mapped = False
        instrument += 1

    if not mapped:
        print('Instrument {} not mapped, used {}'.format(string, instrument))

    return instrument


def create_epilog():
    epilog = '==DRUMS:==\n\n'
    for k, v in drums.items():
        epilog += '{} - {}\n'.format(k, v)

    epilog += '\n==INSTRUMENTS:==\n'
    i = 0
    for k, v in instruments.items():
        if i % 8 == 0:
            epilog += '\n{}\n'.format(instrument_categories[int(i/8)])
        i += 1
        if k not in not_mapped_instruments:
            epilog += '{} - {}\n'.format(k, v)

    return epilog


parser = ArgumentParser(
    formatter_class=RawTextHelpFormatter,
    description='midi_headache - generate headache with midi melody',
    epilog=create_epilog())

parser.add_argument(
    'file_name',
    type=file_type,
    help='output midi file')

parser.add_argument(
    '--tempo', '-t',
    type=tempo_type,
    default=tempo_type(randint(10, 40)*10),
    help='melody tempo in beats per minute')

parser.add_argument(
    '--bars', '-b',
    type=bars_type,
    default=bars_type(8),
    help='length of the melody, 1 bar = 16 beats')

parser.add_argument(
    '--drum', '-d',
    type=drum_type,
    default=drum_type(randint(35, 81)),
    help='drum sound [35-81]')

parser.add_argument(
    '--main', '-m',
    type=instrument_type,
    default=instrument_type(randint(0, 125)),
    help='''main melody instrument [0-125]''')

parser.add_argument(
    '--chords', '-c',
    type=instrument_type,
    default=instrument_type(randint(0, 125)),
    help='chords instrument [0-125]')

parser.add_argument(
    '--extra', '-e',
    type=instrument_type,
    default=instrument_type(randint(0, 125)),
    help='extra instrument [0-125]')
