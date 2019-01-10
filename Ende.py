again = "y"
while again == "y":
    print(" Encrypt and decrypt files:\n")
    print(" [1] Encrypt the file.")
    print(" [2] Decrypt the file.")
    print(" [3] Back.\n")
    s = input(" What do you do Encrypt=1 or Decrypt=2 or Back=3 : ")
    if(int(s) == 1):
        spath = input("\nThe file path link : ")
        f = open(spath, 'rb')
        file_content = f.read()
        f.close()
        ss1 = file_content[0:1000]
        ss2 = file_content[30:50]
        ss3 = file_content[1000:]
        open(spath, 'wb').write(ss2+ss1+ss3+ss2)
        print(" \nFile successfully encrypted..")
    if(int(s) == 2):
        spath1 = input("\nThe file path link : ")
        f1 = open(spath1, 'rb')
        file_content1 = f1.read()
        f1.close()
        ss11 = file_content1[20:1000]
        ss31 = file_content1[1000:-20]
        open(spath1, 'wb').write(ss11+ss31)
        print(" \nFile successfully decrypted..")
    if(int(s) == 3):
        exit()
