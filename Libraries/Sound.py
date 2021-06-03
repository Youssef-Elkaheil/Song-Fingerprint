import os
import librosa

import winsound

from soundfile import SoundFile as sf

class Sound():
    # read wav file
    # returns sampling rate and sound data

    @staticmethod
    def ReadFile(file_name):
        data, SampleRate = librosa.load(file_name, duration=60)
        # get first min
        return data, SampleRate

    @staticmethod
    def CreateSoundFile(arr_of_realNum, samplrate, fileName):
        file_handle = sf(fileName, mode='w', samplerate=samplrate, channels=1,
                         subtype=None, endian='FILE', format='WAV', closefd=True)
        file_handle.write(arr_of_realNum)
        file_handle.close()

    @staticmethod
    def PlaySoundFile(file_name="MixedSong.wav"):
        winsound.PlaySound(file_name, winsound.SND_FILENAME)
        os.remove(file_name)

    def mix(songs, SamplingRate, weight):
        MixedData = (songs[0] * weight) + (songs[1] * (1 - weight))
        Sound.CreateSoundFile(
            MixedData,SamplingRate, "MixedSong.wav")
        return os.path.abspath("MixedSong.wav")
