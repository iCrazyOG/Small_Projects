import turtle,random,time

class Incomplete(Exception):
    pass
class TooManyLetters(Exception):
    pass

def create_Display(word):
    '''Creates the blank list'''
    final=[]
    comparer=[]
    alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
             'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
             'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
             'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
    #adding  either _, a space or the number/symbol
    space_counter=0
    for x in word:
        if x in alphabets:
            final.append('_')
            
        elif x==" ":
            final.append(" ")
            space_counter+=1
            if space_counter>1:
                final.append("\n")
        else:
            final.append(x)
        comparer.append(x)
    
    '''Face, body, leg, leg, hand, hand, eye, eye=8'''
    turt=turtle.Turtle()
    bg=turtle.Screen()
    bg.bgcolor("#b9baa3")
    turt.color("#902923")
    turt.hideturtle()
    
    turt.penup()
    turt.right(180)
    turt.forward(150)
    turt.left(90)
    turt.forward(200)
    turt.left(90)
    turt.pendown()
    
    turt.forward(50)  
    turt.backward(100)
    turt.forward(50)
    turt.left(90)
    turt.forward(350)
    turt.right(90)
    turt.forward(150)
    turt.right(90)
    turt.forward(75)
    turt.speed(0)
    turt.right(90)
    
    
    
    
    return final,comparer,turt

def replace(dsply,fnl,fnl2,guess):
    guess_l=guess.lower()
    final_l=fnl2
        

    for a in range (0,len(fnl)):
        if guess_l==final_l[a]:
            dsply[a]=fnl[a]
            
    return dsply

def generate(time,turt):
    if time==1:
       turt.circle(25,360+180,500)
    elif time==2:
       turt.right(90)
       turt.forward(100)
       turt.right(180)
    elif time==3:
        turt.left(150)
        turt.forward(80)
        turt.backward(80)
    elif time in(4,6):
        turt.left(60)
        turt.forward(80)
        turt.backward(80)
    elif time==5:
        turt.right(30)
        turt.backward(80)
        turt.right(30)
        turt.forward(80)
        turt.backward(80)
    
        

       
      

def hangman(ideal):
    display,final,mover=create_Display(ideal)
    chance=0
    wrong=[]
    final_l=""
    for b in final:
        final_l+=b.lower()
    
    while display!=final and chance<7:
        print((" ".join(display)+"\n"))
        
        try:
            guess=input("Enter your guess\n")
        except Incomplete:
            print ("Error: did not enter an input")
        except TooManyLetters:
            print("Too many letters entered. Please enter only one letter")
        except:
            print("Error")
        else:
            if guess in display:
                print("Already guessed this letter")
            elif guess in final or guess.lower() in final or guess in final_l:
                display=replace(display,final,final_l,guess)
            else:
                if guess not in wrong:
                    wrong.append(guess) 
                chance+=1
                print("Letters not in the word:")
                print(", ".join(wrong))
                generate(chance,mover)
    else:
        generate(chance,mover)
        if chance>=7:
            print("Game over\nThe word was "+ideal)
        else:
            print("CONGRATULATIONS! YOU WON!")
            
        


        
if __name__=="__main__":
    flag=True
    while flag:
        try:
            choice=input("Do you want to play with a preset word or a custom word?\n")
            if ("custom") in choice:
                word=input("Enter a word\n")
                if word=="":
                    raise  Incomplete
            elif ("preset") in choice:
                all_words =["Quixotic", "Cacophony", "Epistemology", "Xenophobia", "Zephyr", "Ubiquitous", "Sycophant", "Obfuscate", "Mnemonic", "Pernicious", "Facetious", "Ebullient", "Serendipity", "Ineffable", "Lethargic", "Munificent", "Disparate", "Dissonant", "Esoteric", "Mellifluous", "Apple", "Dog", "Cat", "Fish", "Bird", "Tree", "House", "Sun", "Book", "Ball", "Water", "Table", "Paper", "Music", "Happy", "Candy", "World", "Phone", "Game", "Sun"]
                word=all_words[random.randint(0,len(all_words)-1)]
            else:
                raise Exception
                
        except Incomplete:
            print ("Error: did not enter an input")
        except:
            print ("An error occurred")
            
        else:
            hangman(word)
        try:
            again=input("\nWould you like to continue playing? (yes/no)\n")
            if again=="yes":
                pass
            elif again=="no":
                flag=False
            else:
                raise Exception
        except:
            print("Error, enter valid word")