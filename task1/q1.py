from hashlib import sha256


hash_of_preceding_coin = "a9c1ae3f4fc29d0be9113a42090a5ef9fdef93f5ec4777a008873972e60bb532"
id_of_miner = sha256("19703057".encode('utf-8')).hexdigest()
print(id_of_miner)
i = 0
while True:
    coin_blob = str(i)
    test_string = "CPEN 442 Coin" + "2021" + hash_of_preceding_coin + coin_blob + id_of_miner

    hashed_text = sha256(test_string.encode('utf-8')).hexdigest()
    if hashed_text[0:8] == "00000000":
        print(coin_blob)
        print(hashed_text)
        break
    if (i % 10000 == 0):
        print(i)
    
    i = i + 1

