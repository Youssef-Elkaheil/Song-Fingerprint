from Database import Database

database = Database.read("DataBase.json")

for i in database:
    # print(i)
    print(database[i])
    # print(database[i]['spectrogram_hash'])
