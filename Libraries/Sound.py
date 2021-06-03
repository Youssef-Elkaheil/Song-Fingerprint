import os
import librosa
import imagehash
import winsound
from PIL import Image
from imagehash import hex_to_hash
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
    def create_dict(song_name, Hashes):
        song = {
            song_name: {
                "spectrogram_hash": Hashes[0],
                "melspectrogram": Hashes[1],
                "mfcc": Hashes[2],
                "chroma_stft": Hashes[3]
            }
        }
        return song

    @staticmethod
    def Hash(array):
        arr = Image.fromarray(array)
        hash = imagehash.phash(arr, hash_size=16).__str__()
        return hash
        
    @staticmethod
    def HashDifference(songhash,databasehase):

        return hex_to_hash(songhash) - hex_to_hash(databasehase)

    @staticmethod
    def PlaySoundFile(file_name="MixedSong.wav"):
        winsound.PlaySound(file_name, winsound.SND_FILENAME)
        os.remove(file_name)

    def mix(songs, SamplingRate, weight):

        MixedData = (songs[0] * weight) + (songs[1] * (1 - weight))
        Sound.CreateSoundFile(
            MixedData,SamplingRate, "MixedSong.wav")
        return os.path.abspath("MixedSong.wav")
