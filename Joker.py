import os
import string
import random
import base64

speclettersandnums = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890_"
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
lettersandnums = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890"
print("Joker By Flamestyx#2076 \ Github3742")
print("")
print("1. Fake Email List w Pass")
print("2. Fake Email List no Pass")
print("3. Fake Discord Token List")
print("")
choice = input("Choice: ")

def id_generator(size=6, chars=string.ascii_lowercase + string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def fakeemwpass():
    os.system("cls")
    endingrandomquery = input("What should the ending be of the email? (e.g gmail.com) If left empty it will be random: ")
    passquery = input("What should the password be? If left empty it will be random: ")
    if endingrandomquery == "":
        os.system("cls")
        amount = input("Amount: ")
        amount2 = int(amount)
        #writing
        if passquery == "":
            for i in range(amount2):
             f = open("emails.txt", "a")
             ses = id_generator(10, letters)
             sas = id_generator(7, letters)
             sus = id_generator(5, lettersandnums)
             f.write(ses + "@" + sas + ".com : "+ sus)
             f.write("\n")
             f.close()
        else:
             for i in range(amount2):
                f = open("emails.txt", "a")
                ses = id_generator(10, letters)
                sas = id_generator(7, letters)
                f.write(ses + "@" + sas + ".com : " + passquery)
                f.write("\n")
                f.close()
    else:
      os.system("cls")
      amount = input("Amount: ")
      amount2 = int(amount)
      #writing
      if passquery == "":
        for i in range(amount2):
            f = open("emails.txt", "a")
            ses = id_generator(10, letters)
            sus = id_generator(5, lettersandnums)
            f.write(ses + "@" + endingrandomquery + " : " + sus)
            f.write("\n")
            f.close()
      else:
        for i in range(amount2):
            f = open("emails.txt", "a")
            ses = id_generator(10, letters)
            sus = id_generator(5, lettersandnums)
            f.write(ses + "@" + endingrandomquery + " : " + passquery)
            f.write("\n")
            f.close()

        
def fakeemnopass():
    os.system("cls")
    endingrandomquery = input("What should the ending be of the email? (e.g gmail.com) If left empty it will be random: ")
    if endingrandomquery == "":
        os.system("cls")
        amount = input("Amount: ")
        amount2 = int(amount)
        #writing
        for i in range(amount2):
            f = open("emails.txt", "a")
            ses = id_generator(10, letters)
            sas = id_generator(7, letters)
            f.write(ses + "@" + sas + ".com")
            f.write("\n")
        f.close()
    else:
        os.system("cls")
        amount = input("Amount: ")
        amount2 = int(amount)
        #writing
        for i in range(amount2):
            f = open("emails.txt", "a")
            ses = id_generator(10, letters)
            f.write(ses + "@" + endingrandomquery)
            f.write("\n")
            f.close()

def discordtoken(notagrabber):
    os.system("cls")
    amount = input("Amount: ")
    amount2 = int(amount)
    for i in range(amount2):
        f = open("tokens.txt", "a")
        id = random.randint(100000000000000000, 999999999999999999)
        message = str(id)
        message_bytes = message.encode('ascii')
        base64_bytes = base64.b64encode(message_bytes)
        base64_message = base64_bytes.decode('ascii')
        sis = id_generator(6, speclettersandnums)
        sos = id_generator(27, lettersandnums)
        f.write(base64_message + "." + sis + "." + sos)
        f.write("\n")
        f.close()



if (choice == "1"):
    fakeemwpass()
elif (choice == "2"):
    fakeemnopass()
elif (choice == "3"):
    discordtoken("thisisntagrabberustalker")


