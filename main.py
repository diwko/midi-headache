from melody_creator import MelodyCreator
from melody_parts_generator import generate_drum_pattern,\
    generate_chord_pattern, generate_pattern
from random import randint
from args_parser import parser


def main():
    args = parser.parse_args()
    melody = MelodyCreator(args.file_name, args.tempo)
    melody.add_drum_pattern(
        generate_drum_pattern(
            args.bars, args.drum, 2**randint(0, 4), 100))

    melody.add_instrument(args.main)
    melody.add_instrument_pattern(
        generate_pattern(
            args.bars, randint(4, 6), (1, 2, 4, 8), randint(1, 10)/10.0, 127))

    melody.add_instrument(args.chords)
    melody.add_instrument_pattern(
        generate_chord_pattern(
            args.bars, randint(4, 6), 2**randint(2, 3), 80))

    melody.add_instrument(args.extra)
    melody.add_instrument_pattern(
        generate_pattern(
            args.bars, randint(4, 6), (1, 2, 4, 8), randint(1, 10)/10.0, 100))

    melody.save_melody()

main()
