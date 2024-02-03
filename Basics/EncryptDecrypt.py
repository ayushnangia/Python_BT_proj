import random
import string

total_set = " "+string.digits+string.ascii_letters+string.punctuation
total_set = list(total_set)
key = total_set.copy()
random.shuffle(key)

def Encrypt():
    inp = input("Enter text: ")
    out = ""
    for i in inp:
        a = total_set.index(i)
        out += key[a]

    print(out)
    print()

def Decrypt():
    inp = input("Enter text: ")
    out = ""
    for i in inp:
        a = key.index(i)
        out += total_set[a]
    
    print(out)
    print()

def Key():
    print(key)
    print()


while True:
    print("1. Encryption\n2. Decryption \n3. Key")
    print()
    m = int(input("Enter mode: "))
    print()
    if m == 1:
        Encrypt()
    elif m == 2:
        Decrypt()
    elif m == 3:
        Key()
    else:
        print("Invalid Mode")

    c = input("Continue? ")
    if c.lower() == "no":
        break
