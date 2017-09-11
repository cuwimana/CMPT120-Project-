tile = "write the title of the game here"
intro = "Write the introduction of the game here -- backstory"

player = ""
initial_loation = ""
player_score = 0

location1 = "Describe location 1"
location2 = "Describe location 2"
location3 = "Describe location 3"
location4 = "final"

start = input("press enter to continue .. ")
while True:
    new_location = input("Which direction do you want to go?")
    
    if new_location == location4:
        print("game conclusion story...")
        print("Display copyright, name, and email")
        break
