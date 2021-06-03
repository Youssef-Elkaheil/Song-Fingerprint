from Libraries.Database import Database

database = Database.read("DataBase.json")

for i in database:
    print(i{"spectrogram_hash"})
