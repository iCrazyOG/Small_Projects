'''
I saw this in a reel, and decided to try and make it myself
'''

import time, random, string

alphabet=[' ']
for a in string.printable:
    alphabet.append(a)
    
def word_gen():
    target=input("Enter a word\n")
    final=""
    while(True):
        choice=input("Do you want the basic version or cool version?\n")
        if (choice.lower().find("cool")==-1) and (choice.lower().find("basic")==-1):
            print("try again")
        else:
            break
        
    if choice.lower().find("cool")>-1:
        while (final!=target):
            for b in range(0,len(target)):
                c=random.choice(alphabet)
                print(final+c)
                time.sleep(0.01)
                if (final+c)==target[0:len(final+c)]:
                    final=final+c
                if target==final:
                    break
    else:
        while (final!=target):
            for b in alphabet:
                print(final+b)
                time.sleep(0.01)
                if (final+b)==target[0:len(final+b)]:
                    final=final+b
                if target==final:
                    break
                
while (True):
    word_gen()
    again=input("Yes or No: Do you want to go again?\n")
    if ("no" in again.lower()):
        print("Thank you!")
        break;
        
    
