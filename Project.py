# Project4   
# Author: Charlotte Uwimana
# 13 November, 2017


import time
# get user input and return name
#no arguments
def getUserInput(): 
    name = input("Enter your name please to continue: ") #input name
    return name #return name

# showing introduction of the game, title and backstory
#takes user name as argument
def intro(name): 
    #game title and intro
    title = (        "\n              Magic Place\n"
                 "      ===========================\n")
    backStory = ("You mysteriously found yourself in the middle of a forest. "
                 "While on the forest walking along the beautiful nature, "
                 "you can receive far more that you seek or lose everything. "
                 "You can discover fun, mysterious and adventurous things that you will never forget."
                 "You then realize that you are in a magic places you have"
                 "never seen before and wanted to escape to the real world "
                 "But you can't unless you get to a meseum on the other side of the sea. "
                 "Your job is to get to that museum before five minutes......." )
    #printing out title and intro
    print(title+"\n")
    print('\n') 
    print("Welcome to Magic Place game "+name+"!!! \n")
    print('\n')
    print(backStory+"\n")
    input("Press Enter to continue")
#concluding function showing  copyright and show scores
def conclude(score, name, inventory): 
    end = ("\nOoops! All museum doors are locked themselves. You are stuck in the Museum! "
           "You can only use the key to escape the Museum to the real world")
    copyRight =  "Copyright(c), @Charlotte Uwimana, charlotte.uwimana1@notes.marist.edu"
    print(end+"\n")
    if "key" in inventory:
        print("Good JOb "+name+", you have won the game. You can now use your key to open through the secret door at the museum to the real world.")
    else:
        score = 0
        print("Good JOb "+name+", you tried your best to finish the game. Unfortunately, you're stuck in the museum since you did not collected the key.")
    print("Your Total score is:" , score,"\n")
    print(copyRight)
    
#defining the locations and their descriptions
#takes no arguments
#return list contaiing locations
def locations(): 
    descriptions = [
                ("                FOREST\n"
                   "You are walking in tannin-brown forest. The grass is crispy under your feet. The trees are "
                  "skyscraper tall. Hares are scampering away from you up ahead. The morning stars are shining "
                  "like sliver snowflakes. The peace of the morning is soul soothing. The forest’s smell is fresh "
                  "and organic. You can only feel joy in your heart flourishing like bubble in boiled water. "
                  "But be careful, this forest is not safe. There are strange creatures haunting you. You must get out now...\n")
              , ("           PRISON HOUSE\n"
                  "You are stuck in prison house, in the middle of nowhere. You are caught by creatures, and they "
                  "have taken all your properties. No way to communicate with your family or to escape. There  "
                  "is a tunnel in the north corner of the prison house. This is your time to find a way to escape.\n ")
              , ("              LAKE BANK\n"
                  "You arrive to a bank of a long lake. There are many places that you can enjoy around the lake."
                 "But you need some items that can help you to do so. It is your time to decide how you can find those items and places "
                 " to help you explore more. Or you can stay and enjoy the nature of the lake and risk your life...\n ")
              , ("                 ISLAND\n"
                  "You arrive at the most beautiful island you have ever visited. It is like a fairy-tale garden.Its beaches are "
                  "covered with soft golden sands. It has an ocean flowers and exotic trees. It has a museum of Greek arts and "
                  "crafts. Add to this playful sun’s rays.You can get an unbelievable tint of piece and beauty. The sight is so "
                  "marvelous and relaxing that even the worst thoughts and the most gloomy mood disappear in no time. It is time "
                  "to either move to the Museum or enjoy the beauty of beach. Just so you know, it will get lonely...\n")
              , ("                   CITY\n"
                  "You arrive at a city where the museam is located. The city is right at the beach You can "
                  "hear the sea roaring. You can feel the wind blowing your face. "
                  "The city is so perfect and calm. It is time to get more relaxing, a building a sandcastle, "
                  "and lots of other things to have fun. Remember, for you to escape the mystical world, you must get to the museum...\n ")
              , ("                  MUSEUM\n"
                  "This is house of magic and museum for ancient Greek arts and crafts. You can hear a stranger voice telling: "
                  "\"I am the most interesting person you have ever met, maybe. I am going to tell you my stories and my experiences. "
                  "I may inspire you and you can learn from me. I am a museum full of Greek arts.\" Are you starting to be nervous and wonder "
                  "how museum can speak? I told you this is a magic place. Continue to enjoy, you will explore more. "
                  "Here, you can learn about ways of getting back to your family...\n ")
              , ("                     SMALL TUNNEL\n" 
                  "You are moving under a small tunnel surrounded by big rocks. It really dark and quiet. "
                  "You can only hear the sound of your feet and the beat of your heart. It is scary and "
                  "you do not know where you will end up. You can either go back or continue your journey...\n ")
              , ( "                          CAVE\n"
                  "The path halted and a cave appeared. Ivy wound round the cave and conceal the entrance that is a jagged opening. "
                  "Inside is dim although being lit by two small fires in the corner of the cave. In the Centre is a small roasting "
                  "pot and in the far north corner there is a small woven mat made with dried grass. Cave is dank and the only sound "
                  "you can hear is the dripping water and wind from lake in east of cave. In west there is a small tunnel, "
                  "which may lead you to exciting places...\n ")
              , ("                          RESTAURANT\n"
                 "It is now becoming darker. You are walking toward a fancy restaurant in the whole city. It is a beautiful place full "
                 "of all kinds of food, wins and beers. Enjoy but be careful you. Things here are so expensive "
                 "and this place is not safe especially in the night...\n")
              , ("                          BEACH\n "
                 "You are now enjoying the beauty of the beach. The beach smells fresh, almost like a new ocean breeze air freshener."
                 "The sand is hot and looks like gold blended in with little white specks...\n")
                 ]
    #returning locations descriptions
    return descriptions
def definitions():
    forest = 0
    prisonHouse = 1
    lakeBank = 2
    island = 3
    city = 4
    museum = 5
    tunnel = 6
    cave = 7
    restaurant = 8
    beach = 9
    
    return forest, prisonHouse, lakeBank, island, city, museum, tunnel, cave, restaurant, beach
    
def matrix(current_loc, move):
    # locations
    forest, prisonHouse, lakeBank, island, city, museum, tunnel, cave, restaurant, beach = definitions()

    world = [
            # North       south        west         east
            [ cave,       None,        None ,       prisonHouse] # forest
        ,   [ lakeBank,   None,        forest,      None  ]  # Prison House
        ,   [ island,     prisonHouse, cave,        beach ]  # lake bank
        ,   [ None,       lakeBank,    city,        None  ]  # Island
        ,   [ restaurant, None,        museum,      island]  # city
        ,   [ None,       None,        None,        None  ]  # Museum
        ,   [ museum,     None,        None,        cave  ]  # tunnel
        ,   [ None,       forest,      tunnel,    lakeBank]  # cave
        ,   [ None,       city,        None,      None    ]  # restaurant
        ,   [ None,       None,        lakeBank,  None    ]  # beach
        ]
    
    new_loc = world[current_loc][move]
    return new_loc

def moveTo(current_location, score, visited, locName):
    if current_location not in visited: # check whether current location has been visited or not
        visited.append(current_location) # add in visited list
        score+=5 # add 5 on the score 
    print('\n')
    print(locName[current_location]) # print current location
    return score # return score

def game_loop(name):
    # getting indexes for locations
    forest, prisonHouse, lakeBank, island, city, museum, tunnel, cave, restaurant, beach = definitions()
    # items to collect base on location index
    items = [ "map", "key", " boat", None, None, "rock", None, "mate", None, "blanket"]
    locName = [ "The forest" , "The prison house", "The lake bank", "The island", "The city", "The museum", " A tunnel", " The cave",
                " The restaurant", " The beach"]
#    directions = [ "north", "south", "west", "east"]
    ask_help = "You can only move north, east, south or west from your current location. Enter the directions to move towards."
    world_map = ("\n         Restaurant                  \n"
           "\n                    |                     \n"
           "\n                    |                     \n"
           "\n                    |                     \n"
           " \n Museum --------- City ----------Island  \n" 
           " \n    |                               |    \n"
           " \n    |                               |    \n"
           " \n Tunnel ------- Cave----------Lake Bank-------- Beach\n"
           " \n                  |                 |    \n"
           " \n                  |                 |    \n"
           " \n               Forest---------Prison House \n" )
    
    descriptions = locations()
    current_location = 0 # starting location
    visited = [current_location] # list of locations that have been visited
    inventory = [] # inventory for picked items
    searched = [] # has been searched list
    score = 0
    #initializing location from moveTo function
    score = moveTo(current_location, score, visited, locName)
    start_time = time.time() #start recording time
    while True: # loop for the game
        stop_time = time.time() # variable for tracking end time 
        # check whether the player is running out of time
        if (stop_time - start_time) >= 300: 
            print( " You ran out of time!\n")
            print("Your score is:", score, "\n")
            return 
        # get input --- case insensitive
        move = input("Enter a command: ").strip().lower() 
        # valid moves in list below
        if move in ["north", "east", "south", "west"]: # direction for moving
            if (move == "north"):
                move_num = 0
            elif(move == "south"):
                move_num = 1
            elif (move == "west"):
                move_num = 2
            else:
                move_num = 3 
                
            #update current location when the move is not none
            # None means the move remains on the same place or it's impossible
            if (matrix(current_location, move_num) != None):
                current_location = matrix(current_location, move_num)
            #Museum is the last location
            if locName[current_location] == "The museum":
                conclude(score, name, inventory)
                break
            #updating score and print current location
            #update visited places
            score = moveTo(current_location, score, visited, locName)
        #look prints the full description of the current location
        elif move == "look": 
            print(descriptions[current_location])
        #search for an item to collect
        elif move == "search" or move == "examine": # search items
            item = items[current_location]
            if item == None:
                print("sorry, there is no item in this place!\n")
            else:
                print( "Congratulation! You discovered: ",item) # reveal item 
                searched.append(current_location) # add item location in searched
        #grab item after search
        elif move == "take":
            if current_location in searched:
                if item not in inventory:
                    inventory.append(item)
                    items.remove(item)
                print("You have added the item to your inventory.\n")
            else:
                print("You have not searched this place!\n ")
        # Oh you need help with movement directions?
        elif move == "help":
            print(ask_help)
        # if you haven't collected the map, you can't see it
        elif move == "map":
            if "map" in inventory:
                print(world_map)
            else:
                print(" Sorry, you do not have map in your inventory.") 
        # alright see you score
        elif move == "score":
            print(name, "Your current score is:", score, "\n" )
        # wait... 
        elif move == "quit":
            print("Game exited.")
            print("Score: ",score)
            return
        # your collections
        elif move == "inventory":
            print(inventory)
        else:
            print("Invalid input .\n")

def main():
    # the main function 
    # convergency of all functions
    name = getUserInput()
    intro(name)
    game_loop(name)
    
main()


    


