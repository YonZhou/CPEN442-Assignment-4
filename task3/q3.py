import hashlib

password = "test2"
newfile = open("19703057.program2.q3.exe", "r+b")
##data = newfile.read()
####address = data.find("Z|V.ýc.¡d.4tá«¶Â@þ¼æ".encode(encoding='utf-8').hex())
##address = data.find(b'\x5A\x7C\x56\x0B\xFD\x63\x93\xA1\x64\x12\x34\x74\xE1\xAB\xB6\xC2\x40\xFE\xBC\xE6')
##print(address)

address = 119803

hashed_password = hashlib.sha1(password.encode('ascii')).digest()
newfile.seek(address)
newfile.write(hashed_password)

                    
newfile.close()
