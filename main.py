#! /usr/bin/env python3
"""
PodcastTools is a command line tool for editing audio files. It is designed to
be used for editing podcasts using machine learning. It's only current
functionality is removing duplicate sections of audio.
"""
import click
import utils as u
import stumpy

@click.command()
@click.argument('filename', type=click.File('r'))
@click.argument('seconds', type=click.INT)
def find_repeating_subsequences(filename, seconds):
    """Return a list of records. Each record has the start and end index of the
    reference audio sequence, and a list of start end index pairs for all the
    near matches at least `length` seconds long.
    """
    # Read wav file into numpy array
    sample_rate, data = u.read_wav(filename)
    window_size = sample_rate * seconds
    profile = stumpy.stump(data, window_size)


if __name__ == '__main__':
    find_repeating_subsequences()
