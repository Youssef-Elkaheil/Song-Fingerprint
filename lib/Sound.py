from tempfile import mktemp
from scipy.io import wavfile
from pydub import AudioSegment
from soundfile import SoundFile as sf

class Sound():
    # read wav file
    # returns sampling rate and sound data

    @staticmethod
    def ReadFile(filePath):
        mp3_audio = AudioSegment.from_mp3(filePath)[:60000]
        waveName = mktemp('.wav')
        mp3_audio.export(waveName, format="wav", parameters=["-ac", "1"])
        samplingFreq, audioData = wavfile.read(waveName)
        return audioData, samplingFreq

    @staticmethod
    def CreateSoundFile(arr_of_realNum, samplrate, fileName):
        file_handle = sf(fileName, mode='w', samplerate=samplrate, channels=1,
                         subtype=None, endian='FILE', format='WAV', closefd=True)
        file_handle.write(arr_of_realNum)
        file_handle.close()

    def mix(songs, SamplingRate, weight):
        MixedData = (songs[1] * weight) + (songs[0] * (1 - weight))
        Sound.CreateSoundFile(MixedData,SamplingRate, "MixedSong.wav")
        return MixedData
