import librosa
from PIL import Image
from imagehash import hex_to_hash ,phash
import numpy as np

class Spectrogram():

    @staticmethod 
    def Features(data, sr):       
        stft = librosa.stft(data)
        Spectrum = librosa.power_to_db(np.abs(stft) ** 2)
        melspectro = librosa.feature.melspectrogram(data, sr=sr,)
        mfccs = librosa.feature.mfcc(data.astype('float64'), sr=sr)
        chroma_stft = librosa.feature.chroma_stft(data, sr=sr,)
        
        return [Spectrum,melspectro, mfccs, chroma_stft]

    @staticmethod
    def Hash(array):
        arr = Image.fromarray(array)
        hash = phash(arr, hash_size=16).__str__()
        return hash

    @staticmethod
    def getHammingDistance(songhash, databasehase):

        return hex_to_hash(songhash) - hex_to_hash(databasehase)

    @staticmethod
    def AdjustRange(inputValue: float, inMin: float, inMax: float, outMin: float, outMax: float):
        slope = (outMax-outMin) / (inMax-inMin)
        return outMin + slope*(inputValue-inMin)

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
