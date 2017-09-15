#Projet 1
# Author: Charlotte Uwimana
print(" Welcome to Hidden Box Game!!!")
print()
print (" We live in world of dreams, imagination, challenges, and fear. We like to dream big and to have unlimited wishes. Every morning, we woke up without knowing what will happen tomorrow. We start to think about what do for the day to make our dreams come true. But there one thing we do not consider, life is like a puzzle game. It is a big box made by small parts. But sometime, we ignored those parts and still want to get that big box. How? One thing, we should know there always a hidden box in life that has the key for our future. However, ignoring these small parts, it can make it harder to get that key…… Imagine one day find yourself in your dream school. You have never been there. Around you, there are many buildings and you are curious to get inside them. Unfortunately there is only one thing which will give you access to them. This is your time to find the access....\n"
       "===========================================================================\n")
def main():
    score=0
    locat1=" Arrived on compus. You are in parking lot where you can see all beauty of the compus. You start to feel very impressive anc curious. There many buildings around you but you do not where to go."
    locat2=" The path leads you to your doom. Ahead in that path, you can see a toller build. As you walk toward the building there other two buidings. all of them are closed."
    locat3= " You are standing next to the toller building. Outside door is not locked."
    locat4= " No one is around you. There is only empy desk in front of you and closed door. Trying to open door. No access!!" 
    locat5= " you are downstairs in  toller building. There people eating and you start to feel hungry. No access!!!"
    locat6= " your talking to your advisor. Ask her what you want?"
    locat7= " your standing infront of the comera. You card is almost done." 
    
    print( " Hidden Box Start here\n"
           "Initial score: ", score, "\n")
    Next= input( "Press Enter to contunue")
    print("location:", locat1, "\n")
    score= score+5
    print(" way to go, your score:", score, "\n")
    Next= input("Press Enter to contunue.")

    print("location:", locat2, "\n")
    score=score+5
    print(" your score:", score,"\n")
    Next= input(" Press Enter to contue.")
    
    print("location:",locat3,"\n")
    score=score+5
    print("your score:", score,"\n")
    Next=input( "Press Enter to contue.")
    
    print("location:",locat4,"\n")
    score=score+5
    print("score:", score,"\n")
    Next=input( "Press Enter to contue.")
    
    print("location:",locat5,"\n")
    score=score+5
    print(" your score:", score,"\n")
    Next=input( "Press Enter to contue.")
    
    print("location:",locat6,"\n")
    score=score+5
    print("score:", score,"\n")
    Next=input( "Press Enter to contue.")

    print("Wow!!!! you got ID to access all buildings")
    score=score
    print("Total score:" , score,"\n")
    print("Copyright (c), Charlotte Uwimana, and charlotte.uwimana1@notes.marist.edu")
