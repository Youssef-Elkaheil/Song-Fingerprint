import librosa
import signal
import imagehash
from PIL import Image
import numpy as np

class Spectrogram():

    @staticmethod
    def spectrogram(data):
        stft = librosa.stft(data)
        spectr =librosa.power_to_db(np.abs(stft) ** 2)
        return spectr

    @staticmethod 
    def Features(file_data, sr):       
        spectro = Spectrogram.spectrogram(file_data)
        melspectro = librosa.feature.melspectrogram(file_data, sr=sr,)
        mfccs = librosa.feature.mfcc(file_data.astype('float64'), sr=sr)
        chroma_stft = librosa.feature.chroma_stft(file_data, sr=sr,)
        
        return [spectro,melspectro, mfccs, chroma_stft]
