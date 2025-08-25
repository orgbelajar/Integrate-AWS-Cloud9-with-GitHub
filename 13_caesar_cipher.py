## Fungsi support
def getDoubleAlphabet(alphabet):
    doubleAlphabet = alphabet + alphabet
    return doubleAlphabet
# print(getDoubleAlphabet('ab'))

def getMessage():
    stringToEncrypt = input("Please enter a message to encrypt: ")
    return stringToEncrypt
# print(getMessage())

def getCipherKey():
    shiftAmount = input( "Please enter a key (whole number from 1-25): ")
    return shiftAmount
# print(getCipherKey())


## Fungsi utama untuk enkripsi
def encryptMessage(message, cipherKey, alphabet):
    encryptedMessage = ""
    uppercaseMessage = ""
    uppercaseMessage = message.upper() # Buat pesan yang di enkripsi menjadi kapital sehingga bisa di compare dengan salt
    for currentCharacter in uppercaseMessage: # Loop over the message character
        position = alphabet.find(currentCharacter) # Menemukan indeks karakter setiap message di dalam salt
        newPosition = position + int(cipherKey) # Tambakan indeks karakter dengan chipperKey menjadi final shifting index
        if currentCharacter in alphabet: # Jika sebuah message character ditemukan dalam sebuah aphabet, maka:
            encryptedMessage = encryptedMessage + alphabet[newPosition] # Simpan value baru dalam encryptedMessage
        else: # Jika tidak ditemukan misal: spasi, angka, special char, do this:
            encryptedMessage = encryptedMessage + currentCharacter # Simpan value asli ke dalam encryptedMessage
    return encryptedMessage # Hasil akhir dari function adalah pesan yang terenkripsi di dalam encryptedMessage
    
def decryptMessage(message, cipherKey, alphabet):
    decryptKey = -1 * int(cipherKey) # Geser chiperKey ke posisi semula (ke kiri) sebanyak x (chiperKey * -1)
    return encryptMessage(message, decryptKey, alphabet) # Hasil akhir adalah pesan yang terdekripsi di dalam encryptedMessage
    
    
## Fungsi runner
def runCaesarCipherProgram():
    myAlphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    print(f'Alphabet: {myAlphabet}')
    myAlphabet2 = getDoubleAlphabet(myAlphabet) #ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ as encriptor salt
    print(f'Alphabet2: {myAlphabet2}')
    myMessage = getMessage() # Terima inputan message dari user. Message ini adalah karakter yang akan di encript
    print(myMessage)
    myCipherKey = getCipherKey() # Terima inputan brp banyak shifting cipher dari user. 
    print(myCipherKey)
    myEncryptedMessage = encryptMessage(myMessage, myCipherKey, myAlphabet2) # Eksekusi enkripsi
    print(f'Encrypted Message: {myEncryptedMessage}')
    myDecryptedMessage = decryptMessage(myEncryptedMessage, myCipherKey, myAlphabet2) # Eksekusi dekripsi
    print(f'Decypted Message: {myDecryptedMessage}')
    
    
runCaesarCipherProgram()