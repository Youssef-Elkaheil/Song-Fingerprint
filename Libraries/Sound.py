import librosa
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
    def fn_CreateSoundFile(arr_of_realNum, samplrate, fileName):
        file_handle = sf(fileName, mode='w', samplerate=samplrate, channels=1,
                         subtype=None, endian='FILE', format='WAV', closefd=True)
        file_handle.write(arr_of_realNum)
        file_handle.close()
