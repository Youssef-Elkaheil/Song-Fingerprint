import os
import json
from lib.Sound import Sound
from lib.Spectrogram import Spectrogram

class Database ():

    @staticmethod
    def write(data, filename):
        if not isinstance(filename, str):
            raise Exception("filename must be string!")

        with open(filename, "w") as file:
            file.write(json.dumps(data,indent=4, separators=(",", ":")))

    @staticmethod
    def read(path):
        with open(path) as jsonFile:
            data = json.load(jsonFile)
        for song in data:
            yield song, data[song]

    @staticmethod
    def Update():
        # iterate over songs paths
        songs = {}
        components = ["Full", "Music", "Vocals"]
        Groups = [] 
        for i in range(2,26):
            if i not in (4,6,16,19,22): Groups.append(i)
        for Group_No in Groups:
            for i in range(1,5):
                for component in components:
                    song_name = "Group" + str(Group_No)+"_Song" + str(i) + "_" + component
                    path = os.path.join("F:/workshop/Github/Songs", song_name + ".mp3")
                    data, samplingRate = Sound.ReadFile(path)
                    features = Spectrogram.Features(data,samplingRate)
                    Hashes = []
                    for j in range(4):
                        Hashes.append(Spectrogram.Hash(features[j]))
                    song = Spectrogram.create_dict(song_name,Hashes)
                    songs.update(song)
            print(Group_No)
        Database.write(songs, "DataBase.json")

# Database.Update()
