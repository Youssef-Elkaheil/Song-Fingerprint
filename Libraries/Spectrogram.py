import librosa
from scipy import signal

class Spectrogram():

    @staticmethod 
    def Features(file_data, sr):       
        _, _, colorMesh = signal.spectrogram(file_data, fs=sr, window='hann')
        melspectro = librosa.feature.melspectrogram(file_data, sr=sr,)
        mfccs = librosa.feature.mfcc(file_data.astype('float64'), sr=sr)
        chroma_stft = librosa.feature.chroma_stft(file_data, sr=sr,)
        
        return [colorMesh,melspectro, mfccs, chroma_stft]
