import unittest
from pathlib import Path
from utils import *

class TestGenerateNoise(unittest.TestCase):

    def setUp(self):
        self.filename = Path("test_noise.wav")

    def test_generate_noise(self):
        # Write it
        sample_rate = 48000
        noise = generate_noise(sample_rate=sample_rate)
        write_wav(self.filename, sample_rate, noise)

        self.assertTrue(self.filename.exists())

    def test_sample_rate(self):
        # Write it
        sample_rate = 48000
        noise = generate_noise(sample_rate=sample_rate)
        write_wav(self.filename, sample_rate, noise)

        # Read it
        rate, data = read_wav(self.filename)
        self.assertEqual(sample_rate, rate)
        # self.assertEqual(noise, data)

    def test_duration(self):
        T = 10
        sr = 44100
        noise = generate_noise(sample_rate=sr, T=T)
        write_wav(self.filename, sr, noise)

        rate, data = read(self.filename)
        self.assertEqual(data.shape[0] / rate, T)

    def tearDown(self):
        self.filename.unlink()

if __name__ == '__main__':
    unittest.main()
