import time, random, string
target=input("Enter a word\n")
#target="Hello World"
alphabet=[' ']
for a in string.printable:
    alphabet.append(a)
final=""
choice=input("do you want the basic version or cool version?\n")
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

content=input("\n")
        
    