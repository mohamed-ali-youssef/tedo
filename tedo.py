import subprocess
# Clear the screen
subprocess.call('clear', shell=True)

s0 = "\n"
c1 = "\x1B[32;40m\x1B[5m"#green
c2 = "\x1B[31;40m\x1B[0m"
c3 = "\x1B[33;40m\x1B[1m"#Yaloow
c4 = "\x1B[34;40m\x1B[1m"#Blue
c5 = "\x1B[31;40m\x1B[1m"#Red

l5 = c5+"  _________________________________________________________________"+c2+"\n"
l1 = c5+"  |################################################################|"+c2+"\n"
#l2 = "  ##"+c5+"|"+c2+"          The tool "+c3+"TeDo"+c2+" developed in Python by            "+c5+"|"+c2+"##\n"
l2 = c5+"  |##|"+c2+"                                                          "+c5+"|##|"+c2+"\n"



t1 = c5+"  |##|"+c2+" "+c3+"        $$$$$$$$  $$$$$$  $$$$%.       %$$$%             "+c2+c5+"|##|"+c2+"\n"
t2 = c5+"  |##|"+c2+" "+c3+"           $$     $$      $$   $$    $$     $$           "+c2+c5+"|##|"+c2+"\n"
t3 = c5+"  |##|"+c2+" "+c3+"           $$     $$$$$$  $$    $$  $$       $$          "+c2+c5+"|##|"+c2+"\n"
t4 = c5+"  |##|"+c2+" "+c3+"           $$     $$      $$   $$    $$     $$           "+c2+c5+"|##|"+c2+"\n"
t5 = c5+"  |##|"+c2+" "+c3+"           $$     $$$$$$  $$$$$^      ^$$$^*             "+c2+c5+"|##|"+c2+"\n"
s1 = c5+"  |##|"+c2+" "+c1+"    ____    ____                _____         _     _    "+c2+c5+"|##|"+c2+"\n"
s2 = c5+"  |##|"+c2+" "+c1+"   |  _ \  / _  |              / ___ \       | |   (_)   "+c2+c5+"|##|"+c2+"\n"
s3 = c5+"  |##|"+c2+" "+c1+"   | | \ \/ / | |             / /   \ \      | |    _    "+c2+c5+"|##|"+c2+"\n"  
s4 = c5+"  |##|"+c2+" "+c1+"   | |  \__/  | |            / /_____\ \     | |   | |   "+c2+c5+"|##|"+c2+"\n"
s5 = c5+"  |##|"+c2+" "+c1+"   | |        | |           /  _______  \    | |   | |   "+c2+c5+"|##|"+c2+"\n"
s6 = c5+"  |##|"+c2+" "+c1+"   | |        | |    _     / /         \ \   | |   | |   "+c2+c5+"|##|"+c2+"\n"
s7 = c5+"  |##|"+c2+" "+c1+"   |_|        |_|   (_)   /_/           \_\  |_|   |_|   "+c2+c5+"|##|"+c2+"\n"
l3 = c5+"  |##|"+c2+"                                                          "+c5+"|##|"+c2+"\n"
l6 = c5+"  |##|"+c2+"            "+c4+"E-Mail : ensert.egypt@hotmail.com             "+c5+"|##|"+c2+"\n"
l7 = c5+"  |##|__________________________________________________________|##|"+c2+"\n"
l4 = c5+"  |################################################################|"+c2+"\n\n"
print l5+l1+l2+t1+t2+t3+t4+t5+s1+s2+s3+s4+s5+s6+s7+l3+l6+l7+l4

print " TeDo tool version 1.0"
print " Designed to test networks and discover vulnerabilities that can be exploited by hackers\n"
print " This open source tool is developed by "+c3+"Eng : Mohamed Ali Youssef"+c2+"\n"

again = "y"
while again == "y":
    #Main Console Ubuntu 
    print("Set of choices for network testing..\n\n")
    print(" [1] Search for open ports in hosting!")
    print(" [2] Encrypt and decrypt files")
    print(" [3] Track sources of communication technique " + "\x1B[32;40m\x1B[1m" + "'ASLP'" + "\x1B[31;40m\x1B[0m")
    print(" [4] Exit")
    print("\n")
    sVal = input("Please then type the allotted number : ")
    if(int(sVal) == 1):
        subprocess.call(["python", "tport.py"])
    if(int(sVal) == 2):
        subprocess.call(["python", "Ende.py"])
    if(int(sVal) == 4):
        print("We have been out of the tool we are happy to use your tool "+c3+"TeDo"+c2+"\n\n")
        exit()