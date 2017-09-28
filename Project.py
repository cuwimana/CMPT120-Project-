#Projet 1
# Author: Charlotte Uwimana
# September 15 2017

title = (" Magic Place\n"
         "=====================\n")

backStory = ("In every walk with nature, you can receive far more that you seek or lose everything."
             "You can discover fun, mysterious and adventurous places that you will never forget. One"
             "day you wake up in the morning and walk slowly to enjoy the freedom and nature of the"
             "forest that you used to enjoy hiking. At this moment, things have changed. You are discovering"
             "magic places you have never seen in your life as well as facing many challenges. This will be"
             "your unforgettable moment in your life discovering a magic island that prisoned"
             "you under the museum curve of Greek arts and crafts.......")
            
forest = ("You are walking in tannin-brown forest.  The grass is crispy under your feet. The trees are"
          "skyscraper tall. Hares are scampering away from you up ahead. The morning stars are shining"
          "like sliver snowflakes. The peace of the morning is soul soothing. The forest’s smell is fresh"
          "and organic. You can only feel joy in your heart flourishing like bubble in boiled water."
          "But be careful, this forest is not safe.")

prisonHouse =("You are stuck in prison house, in the middle of nowhere. You are caught by rebels, and they"
              "have taken all your properties. No way to communicate with your family or to escape. There"
              "is a box in the corn of the prison house. This is your time to find a way to escape.")

lakeBank = ("You arrive to the bank of lake. There is a small boat, swimming vest. There is an island"
            "in the east of the lake. It is your time to decide how you can use these materials to enjoy"
            "your exploration. You can either go to explore island or stay and enjoy the nature of the lake.")

island = ("This is a beautiful island, you have ever visited. It is like a fairy-tale garden.Its beaches are"
          "covered with soft golden sands. It has an ocean flowers and exotic trees. It has a museum of Greek arts and"
          "crafts. Add to this playful sun’s rays.You can get an unbelievable tint of piece and beauty. The sight is so"
          "marvelous and relaxing that even the worst thoughts and the most gloomy mood disappear in no time. It is time"
          "to explore either Museum or enjoy the beaty of beach.")

beach = ("You arrive at the beach. You can hear the sea roaring. You can feel the wind blowing your face."
         "The beach is so soothing and calm. It is time to get more relaxing, a building a sandcastle,"
         "and lots of other things to have fun.")

museum = ("This is house of magic and museum for ancient Greek arts and crafts. You can hear a stranger voice telling:"
          "I am the most interesting person you have ever met, maybe. I am going to tell you my stories and my experiences."
          "I may inspire and you can learn from me. I am a museum full of Greek arts. Are you starting to be nervous and wonder"
          "how museum can speak? I told you this is a magic place. Continue to enjoy, you will explore more")
prompt =("Press Enter to continue.\n")
end = "Ooops! All museum doors are locked themselves. Good bye real world, I am stuck in the Museum!"
copyRight =  "Copyright(c), Charlotte Uwimana, and charlotte.uwimana1@notes.marist.edu"
score = 0

print(title)
print()
print(backStory)
print("Welcome to Magic Place game!!! \n")
print ("Initial score: ", score, "\n")
input(prompt)

curLocation = forest
score= score + 5
print(curLocation )
print(" Your score is:", score, "\n")
input(prompt)

curLocation = prisonHouse
score= score + 5
print(curLocation, "\n")
print(" Your score is:", score, "\n")
input(prompt)

curLocation = lakeBank
score= score + 5
print(curLocation, "\n")
print("Your score is:", score, "\n")
input(prompt)

curLocation = island
score= score + 5
print(curLocation, "\n")
print("Your score is:", score, "\n")
input(prompt)

curLocation = beach
score= score + 5
print (curLocation, "\n")
print("Your score is:", score, "\n")
input(prompt)

curLocation = museum
score= score + 5
print(curLocation, "\n")
print("Your score is:", score, "\n")
input(prompt)
      
print(end)
score=score
print("Total score:" , score,"\n")
print(copyRight)
