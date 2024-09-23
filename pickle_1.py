import pickle
def loadData():
    # for reading also binary mode is important
    dbfile = open('DATABASE', 'rb')    
    db = pickle.load(dbfile)
    for keys in db:
        print(keys, '=>', db[keys])
        filename = f"{keys[0:5]}.pkl"
        DataFile = open (filename , 'wb')
        pickle.dump(db[keys],DataFile)
        DataFile.close()
        
    dbfile.close()




if __name__ == '__main__':
    loadData()