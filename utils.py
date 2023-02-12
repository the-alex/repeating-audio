"""
A utility module for reading and editing audio files.
"""

from typing import Tuple
import numpy as np
from scipy.io.wavfile import write, read
from pathlib import Path
import librosa


def generate_noise(sample_rate: int = 44100, T: int = 5) -> np.ndarray:
    """
    Generates a random noise file.
    
    Parameters:
        sample_rate (int): The sample rate of the output
        T            (int): The duration of the output in seconds
        
    Returns:
        np.ndarray: A numpy array of the random noise.
    """

    # Generate random noise
    t = np.linspace(0, T, int(T * sample_rate), endpoint=False)
    noise = np.random.randn(t.size)

    return noise


# TODO Duration is nonesense here -- the file is the length it is. This should
# be refactored into truncating if the file is longer than the duration in
# seconds.
def generate_music(ex_string: str = "choice", duration: int = 10) -> Tuple[np.ndarray, int]:
    """
    Generates a given piece of music for a certain duration.
    
    Parameters:
        ex_string (str): The example name to generate from. Can be a string from librosa.ex().
        duration  (int): The duration of the output in seconds
        
    Returns:
        (np.ndarray, int): A tuple of a numpy array of the audio data, and the sample rate used.
    """

    y, sr = librosa.load(librosa.ex(ex_string), duration=duration)
    return y, sr


def read_wav(filename: Path) -> Tuple[np.ndarray, int]:
    """
    Reads a WAV file and returns a numpy array of the data.
    
    Parameters:
        filename (Path): The path of the WAV file to read.
        
    Returns:
        (int, np.ndarray): A tuple of the sample rate of the file, and a numpy array of the audio data.
    """
    sample_rate, data = read(filename)
    return sample_rate, data


def write_wav(filename: Path, sample_rate: int, data: np.ndarray):
    """
    Writes a numpy array to a WAV file.
    
    Parameters:
        filename      (Path): The path to write a WAV file to.
        sample_rate   (int): The sample rate of the audio data.
        data    (np.ndarray): A numpy array of audio data.
    """

    write(filename, sample_rate, data)

