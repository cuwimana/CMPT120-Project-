# Project5    
# Author: Charlotte Uwimana
# December 1, 2017
import player 
import location
#import time


def locations():
    locations_list = [ location.Locale( "the forest", ("                          FOREST\n"
                  "You are walking in tannin-brown forest. The grass is crispy under your feet. The trees are "
                  "skyscraper tall. Hares are scampering away from you up ahead. The morning stars are shining "
                  "like sliver snowflakes. The peace of the morning is soul soothing. The forest’s smell is fresh "
                  "and organic. You can only feel joy in your heart flourishing like bubble in boiled water. "
                  "But be careful, this forest is not safe. There are strange creatures haunting you. You must get out now...\n") , ["map"]) 
				,   location.Locale( "the prison house", ("           PRISON HOUSE\n"
                  "You are stuck in prison house, in the middle of nowhere. You are caught by creatures, and they "
                  "have taken all your properties. No way to communicate with your family or to escape. There  "
                  "is a tunnel in the north corner of the prison house. This is your time to find a way to escape.\n "), ["key"]) 
				,   location.Locale( "the Lake Bank",( "            LAKE BANK\n"
                  "You arrive to a bank of a long lake. There are many places that you can enjoy around the lake."
                 "But you need some items that can help you to do so. It is your time to decide how you can find those items and places "
                 " to help you explore more. Or you can stay and enjoy the nature of the lake and risk your life...\n "), ["boat", "life jacket"]) 
				,   location.Locale( "the island",    ("                 ISLAND\n"
                  "You arrive at the most beautiful island you have ever visited. It is like a fairy-tale garden.Its beaches are "
                  "covered with soft golden sands. It has an ocean flowers and exotic trees. It has a museum of Greek arts and "
                  "crafts. Add to this playful sun’s rays.You can get an unbelievable tint of piece and beauty. The sight is so "
                  "marvelous and relaxing that even the worst thoughts and the most gloomy mood disappear in no time. It is time "
                  "to either move to the Museum or enjoy the beauty of beach. Just so you know, it will get lonely...\n"), []) 
				,   location.Locale(" the city", ("                   CITY\n"
                  "You arrive at a city where the museam is located. The city is right at the beach You can "
                  "hear the sea roaring. You can feel the wind blowing your face. "
                  "The city is so perfect and calm. It is time to get more relaxing, a building a sandcastle, "
                  "and lots of other things to have fun. Remember, for you to escape the mystical world, you must get to the museum...\n "), []) 
				,   location.Locale("the museum",   ("                  MUSEUM\n"
                  "This is house of magic and museum for ancient Greek arts and crafts. You can hear a stranger voice telling: "
                  "\"I am the most interesting person you have ever met, maybe. I am going to tell you my stories and my experiences. "
                  "I may inspire you and you can learn from me. I am a museum full of Greek arts.\" Are you starting to be nervous and wonder "
                  "how museum can speak? I told you this is a magic place. Continue to enjoy, you will explore more. "
                  "Here, you can learn about ways of getting back to your family...\n "), ["rock"])
				,   location.Locale("the small tunnel", ("            SMALL TUNNEL\n" 
                  "You are moving under a small tunnel surrounded by big rocks. It really dark and quiet. "
                  "You can only hear the sound of your feet and the beat of your heart. It is scary and "
                  "you do not know where you will end up. You can either go back or continue your journey...\n "), [])
				,   location.Locale(" the cave", ( "                          CAVE\n"
                  "The path halted and a cave appeared. Ivy wound round the cave and conceal the entrance that is a jagged opening. "
                  "Inside is dim although being lit by two small fires in the corner of the cave. In the Centre is a small roasting "
                  "pot and in the far north corner there is a small woven mat made with dried grass. Cave is dank and the only sound "
                  "you can hear is the dripping water and wind from lake in east of cave. In west there is a small tunnel, "
                  "which may lead you to exciting places...\n "), [ "mate" ])
				,   location.Locale(" the restaurant",("                          RESTAURANT\n"
                 "It is now becoming darker. You are walking toward a fancy restaurant in the whole city. It is a beautiful place full "
                 "of all kinds of food, wins and beers. Enjoy but be careful you. Things here are so expensive "
                 "and this place is not safe especially in the night...\n"), ["food box"]) 
				,   location.Locale( "the beach",("                          BEACH\n "
                 "You are now enjoying the beauty of the beach. The beach smells fresh, almost like a new ocean breeze air freshener."
                 "The sand is hot and looks like gold blended in with little white specks...\n"),["Blanket", "ticket"])
                                ,   location.Locale("the amusement park", ("                 AMUSEMENT PARK \n"
                 " You are arrived in amusement park. You can enjoy the roll cost, and beautiful nature, and people around you. "
                 " However, make sure that you get insurance to do so.\n"), ["insurance"])
                                ,   location.Locale(" the water fall", ("                      WATER FALL\n "   
                 " the waterfall is quarium-blue, dizzling onto the rock. At its widest point, it is surging and plinging down "
                 " the mountain. It has a beutiful serenity-pool at the botton. you thrown yourself under the waterfall and the" 
                 " coldness of it start make you shuddering. Find the way to get there.\n"), [])
                                ,   location.Locale(" the bridge", ( "                        BRIDGE \n" 
                 " You are walking over the bridge that leads you to the beautiful island\n"), [])

				]
    return locations_list
    
# get user input and return name
#no arguments
def getUserInput(): 
    name = input("Enter your name please to continue: ") #input name
    return player.Player(name)

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
                 "But you can't unless you get to a meseum on the other side of the sea... "
                 "Your job is to get to the museum with one specific item before five minutes." )
    #printing out title and intro
    print(title)
    print() 
    print("Welcome to Magic Place game "+name+"!!!")
    print('\n')
    print(backStory+"\n")
    input("Press Enter to continue")
def conclude(player1): 
    end = ("\nOoops! All museum doors are locked themselves. You are stuck in the Museum! "
           "You can only use the key to escape the Museum to the real world")
    copyRight =  "Copyright(c), @Charlotte Uwimana, charlotte.uwimana1@notes.marist.edu"
    print(end+"\n")
    if "key" in player1.inventory:
        print("Good JOb "+player1.name+", you have won the game. You can now use your key to open through the secret door at the museum to the real world.")
    else:
        player1.score = 0
        print("Good JOb "+player1.name+", you tried your best to finish the game. Unfortunately, you're stuck in the museum since you did not collected the key.")
    print("Your Total score is:" , player1.score,"\n")
    print(copyRight)
    
def definitions(): # index of each location 
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
    amusementPark = 10
    waterFall = 11
    bridge = 12
    return forest, prisonHouse, lakeBank, island, city, museum, tunnel, cave, restaurant, beach, amusementPark, waterFall, bridge

 
def matrix(current_loc, move):
    # locations
    forest, prisonHouse, lakeBank, island, city, museum, tunnel, cave, restaurant, beach, amusementPark, waterFall, bridge = definitions()

    world = [
            # North       south        west            east
            [ cave,       None,        amusementPark , prisonHouse]  # forest
        ,   [ lakeBank,   None,        forest,         None       ]  # Prison House
        ,   [ island,     prisonHouse, cave,           beach      ]  # lake bank
        ,   [ None,       lakeBank,    city,           bridge     ]  # Island
        ,   [ restaurant, None,        museum,         island     ]  # city
        ,   [ None,       None,        None,           None       ]  # Museum
        ,   [ museum,     None,        None,           cave       ]  # tunnel
        ,   [ None,       forest,      tunnel,         lakeBank   ]  # cave
        ,   [ None,       city,        None,           None       ]  # restaurant
        ,   [ bridge,     None,        lakeBank,       None       ]  # beach
        ,   [ None,       waterFall,   None,           forest     ]  # amusement park
        ,   [ amusementPark, None,     None,           None       ]  # waterFall 
        ,   [ None,       beach,       island,         None       ]  # Bridge 
        ]
    
    new_loc = world[current_loc][move]
    return new_loc
def game_loop(player1):
    ask_help = "You can only move north, east, south or west from your current location. Enter the directions to move towards."
    world_map = (
           "\n               Restaurant                                       \n"
           "\n                    |                                           \n"
           "\n                    |                                           \n"
           "\n                    |                                           \n"
           " \n Museum --------- City ----------Island ----------Bridge       \n" 
           " \n    |                               |               |          \n"
           " \n    |                               |               |          \n"
           " \n Tunnel ---------------Cave----------Lake Bank-----Beach       \n"
           " \n                        |                 |                   \n"
           " \n                        |                 |                   \n"
           " \n Amusement park------Forest---------Prison House              \n"
           " \n       |                                                      \n"
           " \n       |                                                      \n"
           " \n  Waterfall                                                   \n")
    
    locations_list = locations()
    current_location_index = 0
    current_location = locations_list[current_location_index]
    print()
    print(current_location.desc)
    current_location.visited = True
    player1.add_score(0)
    player1.move_counter()
    player1.update_loc(current_location)
    
    while True:
        #if player1.move_count == 4:
            #print("You ran out of time")
            #return 
        move = input("Enter command: " ).lower().strip()
        
        if move in ["north", "east", "south", "west"]:
            if (move == "north"):
                move_num = 0
            elif(move == "south"):
                move_num = 1
            elif (move == "west"):
                move_num = 2
            else:
                move_num = 3 
            if (matrix(current_location_index, move_num) != None):
                current_location_index = matrix(current_location_index, move_num)
                current_location = locations_list[current_location_index]
                
                #Museum is the last location
                if current_location.name == "the museum":
                    conclude(player1)
                    break
                elif current_location.visited:
                    print()
                    print(current_location.desc_after)
                else:
                    print()
                    print(current_location.desc)
                    current_location.visited = True
                    player1.add_score(5)
                    player1.move_counter()
                    player1.update_loc(current_location)
            else:
                print("You are still in",current_location.name, "!")

                
        elif move == "look": 
            print(current_location.desc)
        #search for an item to collect
        elif move == "search" or move == "examine": # search items
            item_list = current_location.items
            if item_list != []:
                print( "Congratulation! You discovered: ",item_list) # reveal item 
                current_location.searched = True # add item location in searched
            else:
                print("sorry, there is no item in this place!\n")
    
        # take the items when the current location has been searched 
        elif move == "take":
            if current_location.searched == True: # current location must be searched
                item = input(" Which item do you want to take?:  " ).lower().strip() # user enter item name
                if item in item_list:
                    if item not in player1.inventory: # check if item is in the current location item list
                        player1.take(item) # take the item and add it to player inventory
                        current_location.take(item)
                        print("You have added", item, "to your inventory!")
                else:
                    print(" There is no such item in this location!")
            else:
                print(" You have not searched yet this place!")
        elif move == "drop":
            item = input(" Which items do you want to drop?: ").lower().strip()
            if item in player1.inventory:
                player1.drop(item)
                current_location.drop(item)
                print(" You have removed", item ,  "from your inventory") 
            else:
                print(" ERROR: You do not have that item in your inventory")
                
                         
        # your collections
        elif move == "inventory":
            print(player1.inventory)

        # Oh you need help with movement directions?
        elif move == "help": 
            print(ask_help)
        # if you haven't collected the map, you can't see it
        elif move == "map":
            if "map" in player1.inventory:
                print(world_map)
            else:
                print(" Sorry, you do not have map in your inventory.") 
        # alright see you score
        elif move == "score":
            print(player1.name, "Your current score is:", player1.score, "\n" )
        # wait... 
        elif move == "quit":
            print("Game exited.")
            print("Score: ",player1.score)
            return
        else:
            print("Invalid input .\n")


def main():
    player1 = getUserInput()
    intro(player1.name)
    game_loop(player1)
main()
