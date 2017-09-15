#Projet 1
# Author: Charlotte Uwimana
print(" Welcome to Hidden Box Game!!!")
print()
print (" We live in world of dreams, imagination, challenges, and fear. We like to dream big and to have unlimited wishes. Every morning, we woke up without knowing what will happen tomorrow. We start to think about what do for the day to make our dreams come true. But there one thing we do not consider, life is like a puzzle game. It is a big box made by small parts. But sometime, we ignored those parts and still want to get that big box. How? One thing, we should know there always a hidden box in life that has the key for our future. However, ignoring these small parts, it can make it harder to get that key…… Imagine one day find yourself in your dream school. You have never been there. Around you, there are many buildings and you are curious to get inside them. Unfortunately there is only one thing which will give you access to them. This is your time to find the access....\n"
       "===========================================================================\n")
def main():
    score=0
    locat1=" Parking lot"
    locat2="Doom, no access"
    locat3= "Dinning Hall, no access"
    locat4= " Library, I want to see my advisor"
    locat5= " donneley, where can I get my ID"
    
    print( " Hidden Box Start here\n"
           "Initial score: ", score, "\n")
    Next= input( "Press Enter to contunue")
    print("location:", locat1, "\n")
    score= score+5
    print(" way to go, your score:", score, "\n")
    Next= input("Press Enter to contunue.")

    print("location:", locat2, "\n")
    score=score+5
    print("score:", score,"\n")
    Next= input(" Press Enter to contue.")
    
    print("location:",locat3,"\n")
    score=score+5
    print("score:", score,"\n")
    Next=input( "Press Enter to contue.")
    
    print("location:",locat4,"\n")
    score=score+5
    print("score:", score,"\n")
    Next=input( "Press Enter to contue.")
    
    print("location:",locat5,"\n")
    score=score+5
    print("score:", score,"\n")
    Next=input( "Press Enter to contue.")

    print("Wow!!!! you got ID to access all buildings")
    score=score
    print("Total score:" , score,"\n")
    print("Copyright (c), Charlotte Uwimana, and charlotte.uwimana1@notes.marist.edu")
