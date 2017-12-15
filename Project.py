# Final Project   
# Author: Charlotte Uwimana
# December 15, 2017
import time 
import player 
import location

def locations():
    locations_list = [ location.Locale( "the forest", ("                          FOREST\n"
                  "You are walking in tannin-brown forest. The grass is crispy under your feet. The trees are "
                  "skyscraper tall. The morning stars are shining like sliver snowflakes."
                  "You are just full of joy. But be careful, this forest is not safe."
                  "There are strange creatures haunting you. You must get out now...\n") , ["map", "knife"]) 
				,   location.Locale( "the prison house", ("           PRISON HOUSE\n"
                  "You are stuck in prison cell, in the middle of nowhere. You are caught by creatures, and they "
                  "have taken all your properties. No way to communicate with your family or to escape."
                  " There is a locked door in north and a envelope in the west corner and there is a phone box in west."
                  " You must do everything quietly in order to escape.\n "), ["envelope"]) 
				,   location.Locale( "the lake bank",( "            LAKE BANK\n"
                  "You arrive to a bank of a long lake. There are many places that you can enjoy around the lake."
                  "But you need some items that can help you to do so. It is your time to decide how you can find those items and places "
                 " to help you explore more. Or you can stay and enjoy the nature of the lake and risk your life...\n "), ["boat", "life jacket"]) 
				,   location.Locale( "the island",    ("                 ISLAND\n"
                  "You arrive at the most beautiful island you have ever visited. It is like a fairy-tale garden.Its beaches are "
                  "covered with soft golden sands. It has an ocean flowers and exotic trees. It has a museum of Greek arts and "
                  "crafts. Add to this playful sun’s rays. You can get an unbelievable tint of piece and beauty. The sight is so "
                  "marvelous and relaxing that even the worst thoughts and the most gloomy mood disappear in no time. It is time "
                  "to either move to the Museum or enjoy the beauty of beach. Just so you know, it will get lonely...\n"), []) 
				,   location.Locale("the city", ("                   CITY\n"
                  "You arrive at a city where the museum is located. The city is right at the beach You can "
                  "hear the sea roaring. You can feel the wind blowing your face. "
                  "The city is so perfect and calm. It is time to get more relaxing, a building a sandcastle, "
                  "and lots of other things to have fun. But do not be distructed."
                  "Remember, your goals is to get to the final distination...\n "), []) 
				,   location.Locale("the museum",   ("                  MUSEUM\n"
                  "This is house of magic and museum for ancient Greek arts and crafts. There is a stranger voice telling: "
                  "\"I am the most interesting person you have ever met, maybe. I am going to tell you my stories and my experiences. "
                  "I may inspire you and you can learn from me. I am a museum full of Greek arts.\" Are you starting to be nervous and wonder "
                  "how museum can speak? I told you this is a magic place, you were looking for but you are still outside.\n "), [])
				,   location.Locale("the small tunnel", ("            SMALL TUNNEL\n" 
                  "You are moving under a small tunnel surrounded by big rocks. It really dark and quiet. "
                  "You can only hear the sound of your feet and the beat of your heart. It is scary and "
                  "you do not know where you will end up. You can either go back or continue your journey...\n "), [])
				,   location.Locale("the cave", ( "                          CAVE\n"
                  "The path halted and a cave appeared. Ivy wound round the cave and conceal the entrance that is a jagged opening. "
                  "Inside is dim although being lit by two small fires in the corner of the cave. In the Centre is a small roasting "
                  "pot and in the far north corner there is a small woven mat made with dried grass. Cave is dank and the only sound "
                  "you can hear is the dripping water and wind from lake in east of cave. In west there is a small tunnel, "
                  "which may lead you to exciting places...\n "), [ "mate", "wax box" ])
				,   location.Locale("the restaurant",("                          RESTAURANT\n"
                 "It is now becoming darker. The journal has been long. This is time to take a short break and get something to fresh you"
                 " This is a fancy restraurant in the whole city.  It is a beautiful place full of all kinds of food, wins and beers"
                 " Unfortunately, this place is not safe. In few minutes, it is going to be attacked by thief."
                 " You must get out or get killed.\n"), ["food box"]) 
				,   location.Locale( "the beach",("                          BEACH\n "
                 "You are now enjoying the beauty of the beach. The beach smells fresh, almost like a new ocean breeze air freshener."
                 "The sand is hot and looks like gold blended in with little white specks. This beach has some dangerous animals that"
                "will kill you if you stay. You can fight with them or find your way to escape...\n"),["blanket", "ticket"])
                                ,   location.Locale("the amusement park", ("                 AMUSEMENT PARK \n"
                 " You are arrived in amusement park. You can enjoy the roll cost, and beautiful nature, and people around you. "
                 " However, make sure that you get insurance to do so.\n"), ["insurance"])
                                ,   location.Locale("the water fall", ("                      WATERFALL\n "   
                 " This waterfall is quarium-blue, dizzling onto the rock. At its widest point, it is surging and plinging down "
                 " the mountain. It has a beutiful serenity-pool at the botton. Now, you can enjoy swimming or go back to other place.\n"), [])
                                ,   location.Locale("the bridge", ( "                        BRIDGE \n" 
                 " You are now walking across the bridge that will lead you to the beautiful island. Safe journal , hope to see to the final destination.\n"), [])

				]
    return locations_list
    
# get user input and return name
#no arguments
def getUserInput(): 
    name = input("Enter your name please to continue: ")#input name
    return player.Player(name)

# showing introduction of the game, title and backstory
#takes user name as argument
def intro(name): 
    #game title and intro
    title = (        "\n              Magic Place\n"
                 "      ===========================\n")
    backStory = ("All things in life are not granted. The choice you make every day are the ones that lead you to the future. " 
                 + name+ ", you mysteriously found yourself in the middle of a forest. While in this forest, "
                 "You then realize that you are in a magic places you have never seen before."
                 "You can discover fun, mysterious and adventurous things that you will never forget."
                 " And this is where your journey started....!")
    task = ( name + ", your task in this game is to get to the final distination, the museum, and be able to enter. In you journey,"
             "you can collect all meterials that you think that will help you in down road and to enjoy some places. You have limited"
             "time to finish your task. Good luck!!!!!!!")
    #printing out title and intro
    print(title)
    print() 
    print("Welcome to Magic Place game "+name+"!!!")
    print('\n')
    print(backStory+"\n")
    print(task+"\n")
    input("Press Enter to continue")
def conclude(player1): 
    end = ("\n Now you are inside the museum. This is where you have been dreaming to be and working hard to get there!" )
    copyRight =  "Copyright(c), @Charlotte Uwimana, charlotte.uwimana1@notes.marist.edu"
    print(end+"\n")
    print("Good JOb "+player1.name+", you have won the game. You arrived the final destination!\n")
    print("Your Total score is:" , player1.score,"\n")
    print(copyRight)
    return copyRight
    
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

# update the score and print out the current location
def moveTo(player1,current_location):
    if current_location.visited:
        print()
        print(current_location.desc_after)
    else:
        print()
        print(current_location.desc)
        current_location.visited = True
        player1.add_score(5)
        player1.move_counter()
        player1.update_loc(current_location)
    return player1.current_loc
def initializeGame(player1): # unitial for game 
    locations_list = locations()
    current_location_index = 0
    current_location = locations_list[current_location_index]
    print()
    print(current_location.desc)
    current_location.visited = True
    player1.add_score(0)
    player1.move_counter()
    player1.update_loc(current_location) 
    return locations_list, current_location_index, current_location, current_location.visited, player1.move_counter 
def game_loop(player1):
    used_items = []
    opened_items = []
    god_help = ("All Might God, help me in this journey so that I can finish it on time."
           "I bielive that even where I am stack wihout knowing what to do, you are always there to hold my hand."
           " Do not let these obstacles block me. Do not let me give up. Amen")

    ask_help = ("You can only move north, east, south or west from your current location." 
                " Other valid commands are: search or examine for finding items, look for looking around the location,"
                "take for additing item on your inventory , use for using items, and drop for removing item you do not want,"
                "converse for talking to someone, other commands: call, pray, climb up, climb down, open. Enter the command to move towards.\n")
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
    
    locations_list,current_location_index, current_location, current_location.visited, player1.move_counter = initializeGame( player1)
    start_time = time.time() # start recording time 
    while True:
        stop_time = time.time() # variable to track end time
        if (stop_time - start_time) >=300:
            print(" Sorry, you rane out of time! Try again later. \n")
            print(" Your score is: ", player1.score, "\n")
            return
        # get input --- case insensitive 
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
                #make sure boat exist if going from lank bank to island
                #The lake bank is secure --> you cannot go to the lake bank without lake 
                if(current_location.name == "the lake bank" and 
                   matrix(current_location_index, move_num) == 3 and 
                   "boat" and "life jacket" not in used_items):
                    print("RESTRICTED: You need to use both a boat and life jacket to cross from the lake bank to the island")
                    continue
                
                #make prison house a  secure location
                #the prison house contains an envelop which access code and key
                #the player needs the access code to escape the prison house
                if current_location.name == "the prison house":
                    if "1234" in player1.inventory and "1234" not in used_items:
                        print("You need to open the envelop and then use the access code inside the envelope.")
                        print("Hint: use the 'use' command after opening the envelope and use the access code\n");
                        continue
                    elif "1234" in player1.inventory and "1234" in used_items:
                        print("Continue to next location\n")
                    else:
                        print("You need an access code to escape the prison house.\n")
                        continue
                    
                
                # make sure that to cross the bridge a person has ticket 
                if(current_location.name == "the beach" and
                   matrix(current_location_index, move_num) == 12 and 
                   "ticket" not in used_items):
                    print(" RESTRICTED: You must use a ticket to cross the bridge and go to island.\n")
                    continue
                # make sure that to go to the waterFall the player has insurance and life jacket
                if(current_location.name == "the amusement park" and 
                   matrix(current_location_index, move_num) == 11 and 
                   "insurance" not in used_items):
                    print("RESTRICTED: You must use insurance, if you want to go to waterfall.\n")
                    continue
                # the final distination, museum. No key, no enter 
                if(matrix(current_location_index, move_num) == 5 and 
                   "envelope" not in player1.inventory):
                    print("The Museum are locked and there is evidently that you do not have key to enter."
                          " To get inside was the goals, so you did not accomplish the goals!\n")
                    reply = input("Play again? yes/no: ").lower().strip()
                    if reply == "yes":
                        player1 = getUserInput()
                        intro(player1.name)
                        game_loop(player1)
                        continue
                    else:
                        print("Thank you for trying. See you soon!!1\n")
                        print("Number of moves: ", player1.move_count) 
                        print("Your current score: ", player1.score)
                        print("Copyright(c), @Charlotte Uwimana, charlotte.uwimana1@notes.marist.edu")
                        break
                current_location_index = matrix(current_location_index, move_num)
                current_location = locations_list[current_location_index]
                update_playerLoc = moveTo(player1,current_location)
                
                if update_playerLoc.name == "the museum":
                    if "envelope" in player1.inventory and "key" not in used_items:
                        print("use the key inside the envelope to get in the museum")
                        print("hint: you must open the envelope first")
                    else:
                        conclude(player1)
                        return
            else:
                print("You are still in",current_location.name, "!")
        
        elif move == "look": 
            print(current_location.desc)
        #search for an item to collect
        elif move == "search" or move == "examine": # search items
            item_list = current_location.items
            if item_list != []:
                print("Congratulation! You discovered: ",item_list, "\n") # reveal item 
                current_location.searched = True # add item location in searched
            else:
                print("No items or items have been taken in this place!\n")
    
        # take the items when the current location has been searched 
        elif move == "take":
            if current_location.searched == True: # current location must be searched
                item = input(" Which item do you want to take?:  " ).lower().strip() # user enter item name
                if item in item_list:
                    player1.take(item) # take the item and add it to player inventory
                    if item == "envelope":
                        player1.take("key")
                        player1.take("1234")
                    current_location.take(item)
                    print("You have added", item, "to your inventory!\n")
                else:
                    print("There is no such item in this location!\n")
            else:
                print("You have not searched yet this place!\n")
        # drop item when it is in your inventory 
        elif move == "drop":
            item = input("Which items do you want to drop?: ").lower().strip()
            if item in player1.inventory: # check if it is in inventory
                player1.drop(item)        # remove it from inventory
                current_location.drop(item) # drop it to the current location
                print("You have removed", item ,  "from your inventory.\n") 
            else:
                print("ERROR: You do not have that item in your inventory.\n")   
                         
        # your collections
        elif move == "inventory":
            print(player1.inventory)

        # Oh you need help with movement directions?
        elif move == "help": 
            print(ask_help)
            
        # if you haven't collected the map, you can't see it
        elif move == "map":
            if "map" in player1.inventory:
                print("You have map in your inventory but you must use it in order to display it.\n")
            else:
                print("Sorry, you do not have map in your inventory.") 
            
        # alright see you score
        elif move == "score":
            print(player1.name, "Your current score is:", player1.score, "\n" )
        # wait... 
        elif move == "quit":
            print("Game exited.")
            print("Score: ",player1.score)
            return
        # your collections
        elif move == "inventory":
            print(player1.inventory)
  
        elif move == "call": # making call, you must be in only prison house. 
            if current_location.name == "the prison house":
                number = input("Enter the phone number: ")
                if 10 <= len(number)<= 15:
                    print("Hello, I am sorry! Now, I am at work and I am not able to repond your call. I will call you later. \n.")
                elif len(number) == 3:
                    print("This is a police office. We are trying to track your location but it seems like it does not exist on earth.\n")
                else:
                    print("The number or code, you dial, is incorrect please check the number or code and call again.\n")  
            else:
                print("There is no phone box in this place.")
        # if player feel lonely can converse with becca 
        elif move == "converse": 
            print("Hello,", player1.name,"!\n"
                  "I am Becca and I am also exploring this magic place. It is a really long journey full of challenges."
                  " But I promise you are not alone. Never give up, you are almost there. \n")
        
        elif move == "open":
            itm = input("what item do you want to open: ").lower()
            if itm in player1.inventory and item == "envelope":
                print("Congrats, you just opened ", itm)
                print(itm, "contains key and access code 1234.\n")
                opened_items.append(itm)
            else:
                print("Your item is not in your inventory or cannot be opened.\n")
                
        # use the items when you have it in the inventory
        elif move == "use":
            # prompt user to enter item he wants to use
            # check if it is in inventory
            itm = input("what item do you want to use: ").lower()
            if itm in player1.inventory:
                if (itm == "key" or itm == "1234") and "envelope" not in opened_items:
                    print("You must open envelope first")
                    continue
                # The key is only used at the museum
                if itm == "key" and current_location.name != "the museum":
                    print("You can only use key at the museum.\n")
                    continue
                #when item is used successfully
                print("You have used", itm ,".")
                print("Access given!!\n" )
                # using key on the museum only
                if itm == "key" and current_location.name == "the museum":
                    conclude(player1)
                    return
                if itm == "map":
                    print(world_map)
                used_items.append(itm)
            else:
                print("Your item is not in your inventory")
        #pray when you do not know what to do
        elif move == "pray":
          print("I know God will understand your prayer.\n")
          print(god_help, "\n")
          
        # Climp up tree when you are in the forest 
        elif move == "climb up":
            if current_location.name == "the forest":
                prompt = input("climp up what?:  ")
                if prompt != "tree":
                    print("I do not understand what you say. \n")
                else:
                    print("You are standing on the top of the branch of tree, six feet above the ground.\n")
            else:
                print("Nothing to climb up.\n")
        elif move == "climb down":
            if current_location == "the forest":
                prompt = input("Form where?: ")
                if prompt != "tree":
                    print("You are already on the ground.\n")
                else:
                    print("You are now under the tree in the forest. You can continue your journey.\n")
            else:
                print("You are already on the ground\n.")
                
        else:
            print("Invalid input .\n")

def main():
    player1 = getUserInput()
    intro(player1.name)
    game_loop(player1)
main()
