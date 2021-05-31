import os
import librosa
from soundfile import SoundFile as sf
from librosa.feature import mfcc, melspectrogram


class Sound():
    # read wav file
    # returns sampling rate and sound data
    @staticmethod
    def ReadFile(file_name):
        data, SampleRate = librosa.load(file_name, duration=60)
        # get first min
        return data, SampleRate

    @staticmethod
    def get_spectrogram(data):
        X = librosa.stft(data)
        Xdb = librosa.power_to_db(abs(X) ** 2)
        # frequancyArr,timeArr,sxx = signal.spectrogram(data, fs=samplerate, window='hann')
        return Xdb

    @staticmethod
    def get_features(data, spectrum, samplingRate):
        feature_1 = melspectrogram(
            y=data, S=spectrum, sr=samplingRate, window="hann")
        feature_2 = mfcc(y=data.astype('float64'), sr=samplingRate)
        return [feature_1, feature_2]

    @staticmethod
    def fn_CreateSoundFile(arr_of_realNum, samplrate, fileName):
        file_handle = sf(fileName, mode='w', samplerate=samplrate, channels=1,
                         subtype=None, endian='FILE', format='WAV', closefd=True)
        file_handle.write(arr_of_realNum)
        file_handle.close()
