# Project5    
# Author: Charlotte Uwimana
# December 1, 2017
import player 
import location
#import time


def locations():
	locations_list = [ location.Locale( "the Forest", ("                          FOREST\n"
                  "You are walking in tannin-brown forest. The grass is crispy under your feet. The trees are "
                  "skyscraper tall. Hares are scampering away from you up ahead. The morning stars are shining "
                  "like sliver snowflakes. The peace of the morning is soul soothing. The forest’s smell is fresh "
                  "and organic. You can only feel joy in your heart flourishing like bubble in boiled water. "
                  "But be careful, this forest is not safe. There are strange creatures haunting you. You must get out now...\n") , ["map"]), 
				location.Locale( "the Prison House", ("           PRISON HOUSE\n"
                  "You are stuck in prison house, in the middle of nowhere. You are caught by creatures, and they "
                  "have taken all your properties. No way to communicate with your family or to escape. There  "
                  "is a tunnel in the north corner of the prison house. This is your time to find a way to escape.\n "), ["Key"]), 
				location.Locale( "the Lake Bank",( "            LAKE BANK\n"
                  "You arrive to a bank of a long lake. There are many places that you can enjoy around the lake."
                 "But you need some items that can help you to do so. It is your time to decide how you can find those items and places "
                 " to help you explore more. Or you can stay and enjoy the nature of the lake and risk your life...\n "), ["Boat"]), 
				location.Locale( "the Island",    ("                 ISLAND\n"
                  "You arrive at the most beautiful island you have ever visited. It is like a fairy-tale garden.Its beaches are "
                  "covered with soft golden sands. It has an ocean flowers and exotic trees. It has a museum of Greek arts and "
                  "crafts. Add to this playful sun’s rays.You can get an unbelievable tint of piece and beauty. The sight is so "
                  "marvelous and relaxing that even the worst thoughts and the most gloomy mood disappear in no time. It is time "
                  "to either move to the Museum or enjoy the beauty of beach. Just so you know, it will get lonely...\n"), [None]), 
				location.Locale(" the city", ("                   CITY\n"
                  "You arrive at a city where the museam is located. The city is right at the beach You can "
                  "hear the sea roaring. You can feel the wind blowing your face. "
                  "The city is so perfect and calm. It is time to get more relaxing, a building a sandcastle, "
                  "and lots of other things to have fun. Remember, for you to escape the mystical world, you must get to the museum...\n "), [None]), 
				location.Locale("the museum",   ("                  MUSEUM\n"
                  "This is house of magic and museum for ancient Greek arts and crafts. You can hear a stranger voice telling: "
                  "\"I am the most interesting person you have ever met, maybe. I am going to tell you my stories and my experiences. "
                  "I may inspire you and you can learn from me. I am a museum full of Greek arts.\" Are you starting to be nervous and wonder "
                  "how museum can speak? I told you this is a magic place. Continue to enjoy, you will explore more. "
                  "Here, you can learn about ways of getting back to your family...\n "), ["Rock"]), 
				location.Locale("the small Tunnel", ("            SMALL TUNNEL\n" 
                  "You are moving under a small tunnel surrounded by big rocks. It really dark and quiet. "
                  "You can only hear the sound of your feet and the beat of your heart. It is scary and "
                  "you do not know where you will end up. You can either go back or continue your journey...\n "), [None]), 
				location.Locale(" the cave", ( "                          CAVE\n"
                  "The path halted and a cave appeared. Ivy wound round the cave and conceal the entrance that is a jagged opening. "
                  "Inside is dim although being lit by two small fires in the corner of the cave. In the Centre is a small roasting "
                  "pot and in the far north corner there is a small woven mat made with dried grass. Cave is dank and the only sound "
                  "you can hear is the dripping water and wind from lake in east of cave. In west there is a small tunnel, "
                  "which may lead you to exciting places...\n "), [ "mate" ]), 
				location.Locale(" the Restaurant",("                          RESTAURANT\n"
                 "It is now becoming darker. You are walking toward a fancy restaurant in the whole city. It is a beautiful place full "
                 "of all kinds of food, wins and beers. Enjoy but be careful you. Things here are so expensive "
                 "and this place is not safe especially in the night...\n"), [None]), 
				location.Locale( "the beach",("                          BEACH\n "
                 "You are now enjoying the beauty of the beach. The beach smells fresh, almost like a new ocean breeze air freshener."
                 "The sand is hot and looks like gold blended in with little white specks...\n"),["Blanket"])
				]
	return locations_list

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

player1 = getUserInput()
intro(player1.name)
