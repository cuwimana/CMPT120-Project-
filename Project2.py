#Projet 1
# Author: Charlotte Uwimana
# September 15 2017


            



def intro():
    title = (        "\n              Magic Place\n"
                 "      ===========================\n")
    backStory = ("You mysteriously found yourself in the middle of a forest."
      "While on the forest walking along the beautiful nature,"
      "you can receive far more that you seek or lose everything."
      "You can discover fun, mysterious and adventurous things that you will never forget."
      "You realize you are in a magic places you have never seen before and wanted to escape to the real world"
      "But you can't unless you get to a meseum on the other side of the sea"
      "Your job is to get to that museum.......")
    print(title+"\n")
    name = input("Enter your name please to continue: ")
    print('\n')
    print("Welcome to Magic Place game "+name+"!!! \n")
    print('\n')
    print(backStory+"\n")
    input("Press Enter to continue")
    print('\n')
    return name

def locations():
    forest = ("                FOREST\n"
        "You are walking in tannin-brown forest.  The grass is crispy under your feet. The trees are"
          "skyscraper tall. Hares are scampering away from you up ahead. The morning stars are shining"
          "like sliver snowflakes. The peace of the morning is soul soothing. The forest’s smell is fresh"
          "and organic. You can only feel joy in your heart flourishing like bubble in boiled water."
          "But be careful, this forest is not safe. There are strange creatures haunting you. You must get out now...")

    prisonHouse =("           PRISON HOUSE\n"
                "You are stuck in prison house, in the middle of nowhere. You are caught by creatures, and they "
                  "have taken all your properties. No way to communicate with your family or to escape. There"
                  " is a tunnel in the north corner of the prison house. This is your time to find a way to escape.")
    
    lakeBank = ( "              LAKE BANK\n"
                "You arrive to a bank of a long lake. There is a small boat, swimming vest. There is an island "
                "in the north of the lake. It is your time to decide how you can use these materials to enjoy "
                "your exploration. You can either go to the island or stay and enjoy the nature of the lake and risk your life")
    
    island = ("                 ISLAND\n"
            "You arrive at the most beautiful island you have ever visited. It is like a fairy-tale garden.Its beaches are"
              "covered with soft golden sands. It has an ocean flowers and exotic trees. It has a museum of Greek arts and"
              "crafts. Add to this playful sun’s rays.You can get an unbelievable tint of piece and beauty. The sight is so"
              "marvelous and relaxing that even the worst thoughts and the most gloomy mood disappear in no time. It is time"
              "to either move to the Museum or enjoy the beauty of beach. Just so you know, it will get lonely...")
    
    city = ("                   CITY\n"
            "You arrive at a city where the museam is located. The city is right at the beach You can hear the sea roaring. You can feel the wind blowing your face."
             "The city is so perfect and calm. It is time to get more relaxing, a building a sandcastle,"
             "and lots of other things to have fun. Remember, for you to escape the mystical world, you must get to the museum")
    
    museum = ("                  MUSEUM\n"
            "This is house of magic and museum for ancient Greek arts and crafts. You can hear a stranger voice telling:"
              "I am the most interesting person you have ever met, maybe. I am going to tell you my stories and my experiences."
              "I may inspire and you can learn from me. I am a museum full of Greek arts. Are you starting to be nervous and wonder "
              "how museum can speak? I told you this is a magic place. Continue to enjoy, you will explore more."
              "Here, you can learn about ways of getting back to your family.")
    return forest, prisonHouse, lakeBank, island, city, museum
    
def conclude(score, name):
    end = "\nOoops! All museum doors are locked themselves. Good bye real world, I am stuck in the Museum!"
    copyRight =  "Copyright(c), @Charlotte Uwimana, charlotte.uwimana1@notes.marist.edu"
    print(end+"\n")
    print('Good JOb '+name+', you have finished the game')
    print("Your Total score is:" , score,"\n")
    print(copyRight)
    




