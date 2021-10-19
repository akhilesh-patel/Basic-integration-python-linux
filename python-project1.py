import os
print("welcome this is my tui program!!!")
os.system("tput setaf 7")
print("..................................")
print(" ")

os.system("tput setaf 4")
while True:
    print("\n ")
    print("""
        press1: date command
        press2: cal command
        press3: web configuration
        press4: create user
        press5: delete user
        press6: exit """)
    os.system("tput setaf 3")
    print(" enter your choice number  ", end = "")
    ch = int(input())
    if ch == 1:
        os.system("date")
    elif ch == 2:
        os.system("cal")
    elif ch == 3:
        os.system("yum install httpd")
    elif ch == 4:
        print("plz type tour user name: ",end='')
        create_user=input()
        os.system("useradd {}".format(create_user))
    elif ch == 5:
        print("plz type your user name:",end='')
        delete_user=input()
        os.system("userdel {}".format(delete_user))
    elif ch == 6:
        os.system(" exit ")
    else:
        print("option  no  support")
        os.system("clear")
~                                                
