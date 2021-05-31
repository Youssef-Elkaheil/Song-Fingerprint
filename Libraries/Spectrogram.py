import librosa
import imagehash
from PIL import Image

class Spectrogram():

    @staticmethod 
    def Features(file_data, sr, spectro):       

        melspectro = librosa.feature.melspectrogram(file_data, sr=sr, S=spectro)
        chroma_stft = librosa.feature.chroma_stft(file_data, sr=sr, S=spectro)
        mfccs = librosa.feature.mfcc(file_data.astype('float64'), sr=sr)

        return [melspectro, mfccs, chroma_stft]

    @staticmethod
    def Hash(feature) -> str:
        data = Image.fromarray(feature)
        return imagehash.phash(data, hash_size=16).__str__()

    
