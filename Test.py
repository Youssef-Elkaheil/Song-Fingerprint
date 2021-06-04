from Database import Database

database = Database.read("DataBase.json")

for songName, songHashes in Database.read("DataBase.json"):
    print(songHashes["spectrogram_hash"])
