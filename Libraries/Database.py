import os
import json
from Libraries.Sound import Sound
from Libraries.Spectrogram import Spectrogram
import signal

class Database ():

    @staticmethod
    def write(data, filename):
        if not isinstance(filename, str):
            raise Exception("filename must be string!")

        with open(filename, "w") as file:
            file.write(json.dumps(data, separators=(",", ":")))

    @staticmethod
    def read(filename=None):
        if not isinstance(filename, str):
            raise Exception("filename must be string!")

        with open(filename, "r") as file:
            data = json.loads(file.read())
        return data

    @staticmethod
    def createDict(file_name):

        Dict = {
            file_name: {"spectrogram_Hash": None,
                        "melspectrogram_Hash": None,
                        "mfcc_Hash": None,
                        "chroma_stft_Hash": None}
        }

        return Dict

    @staticmethod
    #Loads audio file, create a spectrogram, extract some features and hash them.
    def Load_Song(file_name, file_data, sr) -> dict:

        Dict = Database.createDict(file_name)
        f, t, colorMesh = signal.spectrogram(file_data, fs=sr, window='hann')
        features = Spectrogram.Features(file_data, sr, colorMesh)
        data = [["spectrogram_Hash", colorMesh],
                ["melspectrogram_Hash", features[0]], ["mfcc_Hash", features[1]], ["chroma_stft_Hash", features[2]]]

        for i in range(4):
            Dict[file_name][data[i][0]] = Spectrogram.Hash(data[i][1])

        return Dict

    @staticmethod
    def PlotData():

        songs = []
        strings = ["Full", "Music", "Vocals"]
        groups =[2,3,5,7,8,9,10,11,12,13,14,15,16,17,18,20,21,22,23,24,25]
        for group_number in groups:
            count = 1
            for i in range(0, 4):
                arr = []
                for j in strings:
                    path = os.path.join("Songs", "Group" +
                                        str(group_number)+"_Song" + str(count)) + "_" + j + ".mp3"
                    # print(path)
                    # read file
                    data, samplingRate = Sound.ReadFile(path)
                    # get spectrogram
                    spectrum = soundfileUtility.get_spectrogram(data)
                    # hash spectrogram
                    specto_hash = Hash.generate_hash_code(spectrum)
                    features = soundfileUtility.get_features(
                        data, spectrum, samplingRate)

                    feature_1_hash = Hash.generate_hash_code(features[0])
                    feature_2_hash = Hash.generate_hash_code(features[1])

                    song = {
                        "songName": "Group" + str(group_number) + "_Song" + str(count) + "_" + j,
                        "spectrogram_hash": specto_hash,
                        "feature_1": feature_1_hash,
                        "feature_2": feature_2_hash
                    }
                    arr.append(song)
                count += 1
                songs.append(arr)
                print(i)
            print(group_number)
        Database.write(songs, "DB.json")
        
