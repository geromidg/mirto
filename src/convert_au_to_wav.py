#!/usr/bin/env python

"""
.. module:: convert_au_to_wav
   :platform: Unix, Windows
   :synopsis: Contains a function for converting .au tracks to .wav.

.. moduleauthor: Dimitris Geromichalos <geromidg@gmail.com>
"""

from sys import argv
from glob import glob
from scikits import audiolab

def convert_au_to_wav(filename):
    """
    A function for converting audio tracks from .au to .wav.

    Args:
        filename (str): The path of the file to be converted.
    """
    
	au_file = audiolab.sndfile(filename, 'read')

	fmt = audiolab.formatinfo('wav', au_file.get_encoding())
	nchannels = au_file.get_channels()
	fs = au_file.get_samplerate()
	nframes = au_file.get_nframes()
	data = au_file.read_frames(nframes)

	wav_file = audiolab.sndfile(filename[:-2] + 'wav', 'write', fmt, nchannels, fs)
	wav_file.write_frames(data, nframes)
	wav_file.close()

if __name__ == '__main__':
	if len(argv) != 2:
		print 'Usage: %s /path/to/directory/' % (argv[0])
		exit(-1)
		
	for filename in glob(argv[1] + '*.au'):
		convert_au_to_wav(filename)