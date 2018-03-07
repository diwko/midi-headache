from setuptools import setup

setup(name='midi-headache',
      version='0.1',
      description='Midi melody generator.',
      url='http://github.com/diwko/midi-headache',
      author='diwko',
      author_email='dawidsiwko@gmail.com',
      license='MIT',
      packages=['midi_headache'],
      install_requires=[
          'argparse',
          'midiutil'
      ],
      entry_points={
          'console_scripts': ['midi-headache = midi_headache.main:main'],
      },
      zip_safe=False)