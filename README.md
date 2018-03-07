#Midi-Headache
Generate headache with MIDI melody.

#### Install:
```shell
$ pip install git+https://github.com/diwko/midi-headache.git
```

#### Run:
```shell
$ midi-headache FILE_NAME
```
#### Play MIDI melody:
**timidity** can play MIDI files.
```shell
$ timiditi FILE_NAME
```
***
####More options:
  * `-h, --help` -- show this help message and exit
  * `--tempo TEMPO, -t TEMPO`-- melody tempo in beats per minute
  * `--bars BARS, -b BARS` -- length of the melody, 1 bar = 16 beats
  * `--drum DRUM, -d DRUM` -- drum sound [35-81]
  * `--main MAIN, -m MAIN` -- main melody instrument [0-125]
  * `--chords CHORDS, -c CHORDS` -- chords instrument [0-125]
  * `--extra EXTRA, -e EXTRA` -- extra instrument [0-125]

## Treść zadania:

#### Programowanie w jezyku Python 2016/2017 zadanie 1
Uporczywe narkotyczne melodie potrafią czasem na długo przylgnąć do umysłu.
Napisz program, który generuje narkotyczne melodie. Program powinien generować różne melodie w zależności od tego, jakie użytkownik poda opcje. Użytkownik będzie tak długo modyfikował opcje programu aż wygenerowana melodia utkwi mu na stałe w głowie.

Melodie te powinny być generowane w postaci plików midi i zapisywane na dysku twardym, przy czym użytkownik powinien mieć możliwość podania lokalizacji. Obsługa karty dźwiękowej w celu odtworzenia wygenerowanej melodii nie jest konieczna. Można użyć dowolnej biblioteki do obslugi formatu midi, przykladowo https://pypi.python.org/pypi/miditime


Program ten powinien wykorzystywać następujące elementy:
 - klasy
 - funkcje
 - parsowanie argumentów linii poleceń za pomocą modułu argparse ze standardowej biblioteki
 - zewnętrzna biblioteka do obsługi formatu midi
