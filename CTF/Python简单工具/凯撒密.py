def caesar_Crypto(msg):
    '''
    usage:
        caesar_Crypto(msg) ---> to encrypt or decrypt the msg with caesar crypto
    '''
    lowercase = 'abcdefghijklmnopqrstuvwxyz'
    uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    result = []
    offset = 1
    while offset<=26:        
        temp = []
        for char in msg:
            if char in lowercase:            
                temp.append(chr(97 + (ord(char) - 97 + offset) % 26))
            elif char in uppercase:
                temp.append(chr(65 + (ord(char) - 65 + offset) % 26))
            else:
                temp.append(char)
        string = "".join(temp)
        print "[*]offset %d---------"%offset,string
        result.append(string)
        offset += 1
    return result