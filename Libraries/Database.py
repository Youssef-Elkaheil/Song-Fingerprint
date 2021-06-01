import os
import json
import imagehash
from PIL import Image
from Sound import Sound
from Spectrogram import Spectrogram

class Database ():

    @staticmethod
    def write(data, filename):
        if not isinstance(filename, str):
            raise Exception("filename must be string!")

        with open(filename, "w") as file:
            file.write(json.dumps(data,indent=4, separators=(",", ":")))

    @staticmethod
    def read(filename=None):
        if not isinstance(filename, str):
            raise Exception("filename must be string!")

        with open(filename, "r") as file:
            data = json.loads(file.read())
        return data

    @staticmethod
    def Hash(array):
        arr = Image.fromarray(array)
        hash = imagehash.phash(arr, hash_size=16).__str__()
        return hash
        
    @staticmethod
    def PlotData():
        # iterate over songs paths
        songs = []
        strings = ["Full", "Music", "Vocals"]
        # groups = [24]
        groups = [24]
        for group_number in groups:
            count = 1
            for i in range(0, 4):
                arr = []
                for j in strings:
                    path = os.path.join("Songs", "Group" +
                                        str(group_number)+"_Song" + str(count)) + "_" + j + ".mp3"
                    print(path)
                    # read file
                    data, samplingRate = Sound.ReadFile(path)
                    # get spectrogram
                    spectrum = Spectrogram.spectrogram(data)
                    # hash spectrogram
                    specto_hash = Database.Hash(spectrum)
                    features = Spectrogram.Features(
                        data,samplingRate ,spectrum )

                    feature_1_hash = Database.Hash(features[0])
                    feature_2_hash = Database.Hash(features[1])

                    song = {
                        "songName": "Group" + str(group_number) + "_Song" + str(count) + "_" + j,
                        "spectrogram_hash": specto_hash,
                        "feature_1": feature_1_hash,
                        "feature_2": feature_2_hash
                    }
                    arr.append(song)
                count += 1
                songs.append(arr)
            print(group_number)

        Database.write(songs, "DataBase.json")
Database.PlotData()
