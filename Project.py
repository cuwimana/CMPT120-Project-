

#Projet 1
# Author: Charlotte Uwimana
# October 27 2017

import time 
def getUserInput():
    name = input("Enter your name please to continue: ")
    return name

def intro(name): # showing introduction of the game, title and backstory and return name

    title = (        "\n              Magic Place\n"
                 "      ===========================\n")
    backStory = ("You mysteriously found yourself in the middle of a forest."
      "While on the forest walking along the beautiful nature,"
      "you can receive far more that you seek or lose everything."
      "You can discover fun, mysterious and adventurous things that you will never forget."
      "You realize you are in a magic places you have never seen before and wanted to escape to the real world "
      "But you can't unless you get to a meseum on the other side of the sea. "
      "Your job is to get to that museum before five minutes......." )
    print(title+"\n")
    print('\n') 
    print("Welcome to Magic Place game "+name+"!!! \n")
    print('\n')
    print(backStory+"\n")
    input("Press Enter to continue")
    print('\n')

def locations(): # holding list discriptions and lacation valiables signed to indexes, return locations and descriptions
    descriptions = [
                ("                FOREST\n"
                   "You are walking in tannin-brown forest. The grass is crispy under your feet. The trees are "
                  "skyscraper tall. Hares are scampering away from you up ahead. The morning stars are shining "
                  "like sliver snowflakes. The peace of the morning is soul soothing. The forest’s smell is fresh "
                  "and organic. You can only feel joy in your heart flourishing like bubble in boiled water. "
                  "But be careful, this forest is not safe. There are strange creatures haunting you. You must get out now...")
              , ("           PRISON HOUSE\n"
                  "You are stuck in prison house, in the middle of nowhere. You are caught by creatures, and they "
                  "have taken all your properties. No way to communicate with your family or to escape. There  "
                  "is a tunnel in the north corner of the prison house. This is your time to find a way to escape. ")
              , ("              LAKE BANK\n"
                  "You arrive to a bank of a long lake. There is a small boat, swimming vest. There is an island  "
                  "in the north of the lake. It is your time to decide how you can use these materials to enjoy  "
                  "your exploration. You can either go to the island or stay and enjoy the nature of the lake and risk your life. ")
              , ("                 ISLAND\n"
                  "You arrive at the most beautiful island you have ever visited. It is like a fairy-tale garden.Its beaches are "
                  "covered with soft golden sands. It has an ocean flowers and exotic trees. It has a museum of Greek arts and "
                  "crafts. Add to this playful sun’s rays.You can get an unbelievable tint of piece and beauty. The sight is so "
                  "marvelous and relaxing that even the worst thoughts and the most gloomy mood disappear in no time. It is time "
                  "to either move to the Museum or enjoy the beauty of beach. Just so you know, it will get lonely...")
              , ("                   CITY\n"
                  "You arrive at a city where the museam is located. The city is right at the beach You can "
                  "hear the sea roaring. You can feel the wind blowing your face. "
                  "The city is so perfect and calm. It is time to get more relaxing, a building a sandcastle, "
                  "and lots of other things to have fun. Remember, for you to escape the mystical world, you must get to the museum ")
              , ("                  MUSEUM\n"
                  "This is house of magic and museum for ancient Greek arts and crafts. You can hear a stranger voice telling: "
                  "I am the most interesting person you have ever met, maybe. I am going to tell you my stories and my experiences. "
                  "I may inspire and you can learn from me. I am a museum full of Greek arts. Are you starting to be nervous and wonder "
                  "how museum can speak? I told you this is a magic place. Continue to enjoy, you will explore more. "
                  "Here, you can learn about ways of getting back to your family. ")
              , ("                     SMALL TUNNEL\n" 
                  "You are moving under a small tunnel surrounded by big rocks. It really dark and quiet. "
                  "You can only hear the sound of your feet and the beat of your heart. It is scary and "
                  "you do not know where you will end up. You can either go back or continue your journey. ")
              , ( "                          CAVE\n"
                  "The path halted and a cave appeared. Ivy wound round the cave and conceal the entrance that is a jagged opening. "
                  "Inside is dim although being lit by two small fires in the corner of the cave. In the Centre is a small roasting "
                  "pot and in the far north corner there is a small woven mat made with dried grass. Cave is dank and the only sound "
                  "you can hear is the dripping water and wind from lake in east of cave. In west there is a small tunnel, "
                  "which may lead you to exciting places. ")
                ]
    forest = 0
    prisonHouse = 1
    lakeBank = 2
    island = 3
    city = 4
    museum = 5
    tunnel = 6
    cave = 7
    return descriptions, forest, prisonHouse, lakeBank, island, city, museum, tunnel, cave  
def conclude(score, name): # show copyright and show scores
    end = "\nOoops! All museum doors are locked themselves. Good bye real world, I am stuck in the Museum!"
    copyRight =  "Copyright(c), @Charlotte Uwimana, charlotte.uwimana1@notes.marist.edu"
    print(end+"\n")
    print('Good JOb '+name+', you have finished the game')
    print("Your Total score is:" , score,"\n")
    print(copyRight)
#def moveTo(current_location):
    
    # set the current location
    # check if visited
    #    if not, add to score, and add to visited
    # print current location
    #return score, current_location
def gameLoop(name): # return score 
    descriptions, forest, prisonHouse, lakeBank, island, city, museum, tunnel, cave = locations()
    # map and help
    ask_help = "You can only move north, east, south or west from your current location. Enter the directions to move towards." 
    map = (" \n Museum --------- City ----------Island  \n" 
           " \n    |                               |    \n"
           " \n    |                               |    \n"
           " \n Tunnel ------- Cave----------Lake Bank  \n"
           " \n                  |                 |    \n"
           " \n                  |                 |    \n"
           " \n               Forest---------Prison House \n" )
 
    current_location = forest # starting location
    visited = [current_location] # tracking locations that have been visited 
    print(descriptions[current_location])
    score = 0
    start_time = time.time() # variable for tracking start time for the gem
    stop_time = time.time() # variable for tracking end time for the game    
    while True: # loop for the game 
        stop_time = time.time() # variable for tracking end time 
        if (stop_time - start_time) >= 300: # check whether the player is running out of time
            print( " You ran out of time!\n")
            print("Your score is:", score, "\n")
            return 
        print("\n")
        #move to getUserInput 
        move = input("Enter a direction: ").strip().lower() # hundle case insensitive
        print("\n")
        if move in ["north", "east", "south", "west"]: # direction for moving 
            if current_location == forest:  # tract movement in the forest 
                if move in ["south", "west"]:
                    print("You are still in the forest.")
                elif move == "east":
                    print("You are captured by wild creatures and put in Prison!\n")
                    current_location = prisonHouse
                elif move == "north":
                    print("You are in the way lead you to the cave!\n")
                    current_location = cave
                if current_location not in visited: # check whether current location has been visited or not
                    visited.append(current_location) # add in visited list
                    score+=5 # add 5 on the score 
                print(descriptions[current_location]) # move this code into the moveTo function, and remove from here and below
            elif current_location == cave: # track movement in the cave
                if move == "north":
                    print("you are still in the cave!\n")
                if move == "south":
                    print("return in the forest!\n")
                    current_location = forest
                if move == "west":
                    print(" you are walking under the small tunnel")
                    current_location = tunnel 
                if move == "east":
                    print("You are walking to ward the lake bank!\n")
                    current_location = lakeBank
                if current_location not in visited:
                    visited.append(current_location)
                    score+=5
                print(descriptions[current_location]) 
            elif current_location == tunnel: # track movement in the tunnel
                if move in ["south", "west"]:
                    print(" you bump into the tunnel wall")
                elif move == "east":
                    print(" You going back in the cave!\n")
                    current_location = cave
                elif move == "north":
                    current_location = museum
                if current_location not in visited:
                    visited.append(current_location)
                    score+=5
                print(descriptions[current_location])
            elif current_location == prisonHouse:
                if move in ["east", "south"]:
                    print("You bump into the prison wall.\n")
                if move == "west":
                    print("Going back into the forest!\n")
                    current_location = forest
                if move == "north":
                    print("you have arrive at a shore of a sea!\n")
                    current_location = lakeBank
                if current_location not in visited: 
                    visited.append(current_location)
                    score+=5
                print(descriptions[current_location])
                    
            elif current_location == lakeBank: # truck movement at lake bank
                if move == "east":
                    print("you are still on the lake bank!\n")
                elif move == "west":
                    print(" The is a beautiful curve in front of you!")
                    current_location = cave
                elif move == "south":
                    print("Going back into the prison house!\n")
                    current_location = prisonHouse
                elif move == "north":
                    print("you are now at an island!\n")
                    current_location = island 
                if current_location not in visited:
                    visited.append(current_location)
                    score+=5
                print(descriptions[current_location])
            elif current_location == island:# truck movement in island 
                if move in ["north", "east"]:
                    print("you are still on the middle of the sea!\n")
                elif move == "south":
                    print("you are going back into the lake bank!\n")
                    current_location = lakeBank
                elif move == "west":
                    print("you are now in the mystical city\n")
                    current_location = city
                if current_location not in visited:
                    visited.append(current_location)
                    score+=5
                print(descriptions[current_location])
            elif current_location == city: # truck movement in the city 
                if move in ["north","south"]:
                    print("You are wandering around the city\n")
                elif move in ["east"]:
                    print("You are going back to the island")
                    current_location = island
                    print(descriptions[current_location])
                elif move == "west":
                    current_location = museum
                if current_location not in visited:
                    visited.append(current_location)
                    score+=5
                print(descriptions[current_location])
  
            if current_location == museum: # ending location 
                break

        elif move == "help":
            print(ask_help)
        elif move == "map":
            print(map)
        elif move == "score":
            print(name, "Your current score is:", score, "\n" )
        elif move == "quit":
            print("Game exited.")
            print("Score: ",score)
            return
        else:
            print("Invalid input .\n")
    return score
def main():
    name = getUserInput()
    intro(name)  
    score = gameLoop(name)
    conclude(score, name)
    
main()


