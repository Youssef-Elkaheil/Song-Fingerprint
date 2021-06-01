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
        components = ["Full", "Music", "Vocals"]
        Groups = [] 
        for i in range(2,26):
            if i not in (4,6,19): Groups.append(i)
        # print(Groups)

        for Group_No in Groups:
            for i in range(1,5):
                Song_components = []
                for component in components:
                    song_name = "Group" + str(Group_No)+"_Song" + str(i) + "_" + component
                    path = os.path.join("Songs",song_name + ".mp3")
                    # read file
                    data, samplingRate = Sound.ReadFile(path)
                    spectrum = Spectrogram.spectrogram(data)
                    features = Spectrogram.Features(
                        data,samplingRate ,spectrum )
                    Hashes = [Database.Hash(spectrum)]
                    for j in range(3):
                        Hashes.append(Database.Hash(features[j]))

                    song = {
                        "songName": "Group" + song_name,
                        "spectrogram_hash": Hashes[0],
                        "melspectrogram": Hashes[1],
                        "mfcc": Hashes[2],
                        "chroma_stft": Hashes[3]
                    }
                    Song_components.append(song)
                songs.append(Song_components)
            print(Group_No)

        Database.write(songs, "DataBase.json")

Database.PlotData()
