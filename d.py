print(''''
 ██░ ██  ▄▄▄        ██████  ██░ ██    
▓██░ ██▒▒████▄    ▒██    ▒ ▓██░ ██▒   
▒██▀▀██░▒██  ▀█▄  ░ ▓██▄   ▒██▀▀██░   
░▓█ ░██ ░██▄▄▄▄██   ▒   ██▒░▓█ ░██    
░▓█▒░██▓ ▓█   ▓██▒▒██████▒▒░▓█▒░██▓   
 ▒ ░░▒░▒ ▒▒   ▓▒█░▒ ▒▓▒ ▒ ░ ▒ ░░▒░▒   
 ▒ ░▒░ ░  ▒   ▒▒ ░░ ░▒  ░ ░ ▒ ░▒░ ░   
 ░  ░░ ░  ░   ▒   ░  ░  ░   ░  ░░ ░   
 ░  ░  ░      ░  ░      ░   ░  ░  ░   
                                                                                                          
''')
import base64
while True :
    num = input("""
    
    1 > Encode
    2 > Decode
    3 > Know The Hash
    >> : """)

    if num == "1":
        encode_text = input("Enter Your Text For Encode It >> : ")
        encode_hash = base64.b64encode(encode_text.encode('UTF-8')).decode('ascii')
        print("_________________________________")
        print("Doen Encode --> "+ encode_hash)
        print("_________________________________")
    if num == "2":
        decode_text = input("Enter Your Hash For Decode It >> :")
        decode_hash = base64.b64decode(decode_text)
        decodeit = decode_hash.decode('UTF-8')
        print("_________________________________")
        print("Doen Decode --> "+ decodeit)
        print("_________________________________")
        
    if num == "3":
        your = input('Enter Ur Hash:')

        x = 0

        for xx in your :
            x = x + 1

        if x == 32 :
            print(your)
            print('____________')
            print('MD5')
            print('____________')
        ##########################
        if x == 40 :
            print(your)
            print('____________')
            print('SHA1')
            print('____________')
        #########################
        if x == 64 :
            print(your)
            print('____________')
            print('SHA256')
            print('SHA3_256')
            print('____________')
        #########################
        if x == 128:
            print(your)
            print('____________')
            print('SHA512')
            print('SHA3_512')
            print('____________')
        #######################
        if x == 56 :
            print(your)
            print('____________')
            print('SHA224')
            print('SHA3_224')
            print('____________')
        #######################
        if x == 96 :
            print(your)
            print('____________')
            print('SHA384')
            print('SHA3_384')
            print('____________')

    else:
        print("write just 1 or 2 or 3 ")
