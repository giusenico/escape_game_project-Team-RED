# define rooms and items

import time   #to allow handling time
import random  # to choose a random number
from random import randint
import pygame
import threading

couch = {
    "name": "couch",
    "type": "furniture",
}

door_a = {
    "name": "door a",
    "type": "door",
}

key_a = {
    "name": "key for door a",
    "type": "key",
    "target": door_a,
}

piano = {
    "name": "piano",
    "type": "furniture",
}

game_room = {
    "name": "game room",
    "type": "room",
}

outside = {
  "name": "outside"
}

q_bed = {
    "name": "queen bed",
    "type": "furniture"
}

door_b = {
    "name": "door b",
    "type": "door"
}

door_c = {
    "name": "door c",
    "type": "door"
}

key_b = {
    "name": "key for door b",
    "type": "key",
    "target": door_b,
}

br1 = {
    "name": "bedroom 1",
    "type": "room",
}
br2 = {
    "name": "bedroom 2",
    "type": "room",
}
## bedroom 1
q_bed = {
    "name": "queen bed",
    "type": "furniture",
}
drw = {
    "name": "drawer",
    "type": "furniture",
}
a_clock = {
    "name": "alarm clock",
    "type": "furniture",
}

living_room = {
    "name": "living room",
    "type" : "room"
}

door_d = {
    "name": "door d",
    "type": "door"
}

table = {
    "name": "table",
    "type": "furniture",
}
key_c = {
    "name": "key for door c",
    "type": "key",
    "target": door_c,
}
key_d = {
    "name": "key for door d",
    "type": "key",
    "target": door_d,
}

key_drw = {
    "name": "key for drawer",
    "type": "key",
    "target": drw,
}

## bedroom 2
d_bed = {
    "name": "double bed",
    "type": "furniture",
}

dresser = {
    "name": "dresser",
    "type": "furniture",
}
all_rooms = [game_room, outside, br1, br2, living_room]

all_doors = [door_a, door_b, door_c, door_d]

# define which items/rooms are related

object_relations = {
    "game room": [couch, piano, door_a],
    "bedroom 1": [q_bed, drw, a_clock, door_c, door_b, door_a],
    "bedroom 2": [d_bed, dresser, door_b],
    "living room" : [table, door_d],
    "queen bed": [key_b],
    "double bed":[key_c],
    "dresser":[key_d],
    "piano": [key_a],
    "outside": [door_d],
    "door a": [game_room, br1],
    "door b": [br1, br2],
    "door c": [br1, living_room],
    "door d": [living_room, outside]
}

# define game state. Do not directly change this dict.
# Instead, when a new game starts, make a copy of this
# dict and use the copy to store gameplay state. This
# way you can replay the game multiple times.

INIT_GAME_STATE = {
    "current_room": game_room,
    "keys_collected": [],
    "target_room": outside
}


def linebreak():
    """
    Print a line break
    """
    print("\n\n")

def start_game():
    """
    Start the game
    """
    print("\nYou wake up on a couch and find yourself in a strange house with no windows which you have never been to before. You don't remember why you are here and what had happened before. You feel some unknown danger is approaching and you must get out of the house, NOW!\n")
    play_room(game_state["current_room"])

def play_room(room):
    """
    Play a room. First check if the room being played is the target room.
    If it is, the game will end with success. Otherwise, let player either
    explore (list all items in this room) or examine an item found here.
    """
    game_state["current_room"] = room
    if(game_state["current_room"] == game_state["target_room"]):
        print("Congrats! You escaped the room!\n")
    else:
        print("\nYou are now in " + room["name"])
        intended_action = input("\nWhat would you like to do? Type 'explore' or 'examine' or 'inventory'?\n").strip()
        if intended_action == "explore":
            explore_room(room)
            play_room(room)
        elif intended_action == "examine":
            examine_item(input("\nWhat would you like to examine?\n").strip())
        elif intended_action == "inventory":
            check_inventory()
            play_room(room)
        else:
            print("Not sure what you mean. Type 'explore' or 'examine'.\n")
            play_room(room)
        linebreak()

def check_inventory():
  list_of_keys = game_state['keys_collected']
  if len(list_of_keys) == 0:
    print("You check your pockets. They don't seem to have left you with any of your belingings.\n")
  else:
    print("\nYou check your pockets, you find:")
    for key in list_of_keys:
      print(key['name'])

def explore_room(room):
    """
    Explore a room. List all items belonging to this room.
    """
    explore_message = "\nYou explore the room. This is " + room["name"] + ". You find "
    for item in object_relations[room["name"]]:
      explore_message += str(item["name"]) + ", "
    explore_message = explore_message[:-2]+"."
    print(explore_message)

def get_next_room_of_door(door, current_room):
    """
    From object_relations, find the two rooms connected to the given door.
    Return the second room.
    """
    connected_rooms = object_relations[door["name"]]

    if connected_rooms[0] == current_room:
      return connected_rooms[1]
    else:
      return connected_rooms[0]
    


def guessTheSongGame():
    # Initialize pygame mixer for playing audio
    pygame.mixer.init()

    # Function to play the song using pygame
    def play_song():
        try:
            # Load and play the audio file
            pygame.mixer.music.load("happy-birthday-jazz-171120.mp3")
            pygame.mixer.music.play()
        except pygame.error as e:
            print(f"Error playing the song: {e}")

    # Start playing the song in a separate thread so the user can guess while it's playing
    song_thread = threading.Thread(target=play_song)
    song_thread.start()

    # Variable to track if the song has been guessed correctly
    songGuessed = False

    # Loop until the song is guessed correctly
    while not songGuessed:
        # Prompt the user to guess the title of the song
        songName = input("\nTo get the key, guess the title of the song: ").lower().strip()

        # Check if the guessed title is correct
        if songName == "happy birthday" or songName == "happybirthday":
            print("The title is correct! You get the key.\n")
            songGuessed = True
        else:
            print("The title is wrong. Try again!\n")

    # Stop the music if it is still playing
    pygame.mixer.music.stop()

    # Wait for the song thread to finish
    song_thread.join()

    # Return the result of the game
    return songGuessed


def guessNumber():
    # Initialize a variable to track if the number has been guessed correctly
    numberGuessed = False

    print("\nIn order to open the door you need to guess the secret number :) (1 to 5) \n")

    randomNumber = randint(1, 5)

    # Loop until the number is guessed correctly
    while not numberGuessed:
        # Inner loop to ensure the input is a valid integer
        while True:
            try:
                answer = int(input("Answer: ").strip())
                break  # Exit the loop if the input is a valid integer
            except ValueError:
                print("Please enter a valid integer. \n")

        if answer == randomNumber:
            numberGuessed = True  # Set the flag to True to exit the loop
            print("You guessed the number! \n")

    # Return the result of the number guessing
    return numberGuessed

def quiz_game():
    quiz_guessed = False  # Flag to track if the correct answer has been guessed

    print("\nQuiz Game! \n")
    print("You are trapped in a room with three doors. Each one leads to a possible escape route, but only one is safe. Here are the options:\n")
    print("Door 1: Behind this door is a fire-breathing dragon.\n")
    print("Door 2: Behind this door is a trap that is activated as soon as you enter.\n")
    print("Door 3: Behind this door is a room full of poisonous snakes.\n")

    while not quiz_guessed:
        while True:
            try:
                # Prompt user to choose a door
                print("Which door do you choose to escape safely? (1 to 3): ")
                answer = int(input("Answer: ").strip())  # Ensure the input is an integer

                if answer == 2 or answer == 3:  # Incorrect answers
                    print("The answer is not correct, try again! \n")
                break  # Exit the loop if the input is a valid integer
            except answer < 1 or answer > 3:  # Check if input is within range
                print("Please enter a number between 1 and 3. \n")
            except ValueError:  # Handle invalid (non-integer) input
                print("Please enter a valid integer. \n")

        # Check if the user chose the correct door
        if answer == 1:
            quiz_guessed = True  # Set the flag to True to exit the loop
            print("Door 1 is the safest, because dragons do not exist! \n")
    
    return quiz_guessed  # Return True if the user has guessed correctly

def dice_roll():
    dice_guessed = False  # Flag to track if the sum of dice rolls is greater than 8

    print("\nDice rolling game! \n")
    print("You have two dice, in order to unlock the door the sum of the roll must be greater than 8")

    while not dice_guessed:
        while True:
            try:
                # Generate random numbers for two dice
                result1 = randint(1, 6)
                result2 = randint(1, 6)

                # Ask the user to press 'k' to roll the dice
                print("Send a 'k' to roll the dice: ")
                answer = input("Insert: ").strip()

                # Display the dice results and the sum
                print("The dice numbers that came out are ", result1, " and ", result2, "\n")
                print("The sum is: ", result1 + result2, "\n")

                # Check if the sum is greater than 8
                if result1 + result2 > 8:
                    dice_guessed = True  # Set the flag to True to exit the loop
                    print("The sum is greater than 8! \n")
                    break
                else:
                    print("The sum is not greater than 8, try again! \n")  
            # Ensure the user enters 'k' to roll the dice
            except answer != 'k':  
                print("Enter 'k' to roll the dice! \n")

    return dice_guessed  # Return True if the sum of dice rolls is greater than 8


def rock_paper_scissors():
    """
    Rock Paper Scissors game for the dresser. Player needs to win to unlock.
    """
    options = ["rock", "paper", "scissors"]
    player_won = False

    while not player_won:
        computer_choice = random.choice(options)
        player_choice = input("Choose rock, paper, or scissors: ").strip().lower()

        if player_choice not in options:
            print("Invalid choice! Please choose rock, paper, or scissors.\n")
            continue

        print(f"You chose {player_choice}, the dresser chose {computer_choice}.")

        if player_choice == computer_choice:
            print("It's a tie! Try again.\n")
        elif (player_choice == "rock" and computer_choice == "scissors") or \
             (player_choice == "paper" and computer_choice == "rock") or \
             (player_choice == "scissors" and computer_choice == "paper"):
            print("You win! The dresser unlocks.\n")
            player_won = True
        else:
            print("You lose! Try again.\n")
            
def linebreak():
    """
    Print a line break
    """
    print("\n\n")


def examine_item(item_name):
    """
    Examine an item which can be a door or furniture.
    First make sure the intended item belongs to the current room.
    Then check if the item is a door. Tell player if key hasn't been
    collected yet. Otherwise ask player if they want to go to the next
    room. If the item is not a door, then check if it contains keys.
    Collect the key if found and update the game state. At the end,
    play either the current or the next room depending on the game state
    to keep playing.
    """
    current_room = game_state["current_room"]
    next_room = ""
    output = None

    # Loop through items in the current room
    for item in object_relations[current_room["name"]]:
        if item["name"] == item_name:
            output = "You examine " + item_name + ". "

            # Handle doors
            if item["type"] == "door":
                if item["name"] == "door a" and guessNumber():
                    pass
                elif item["name"] == "door b" and guessNumber():
                    pass
                elif item["name"] == "door c" and guessNumber():
                    pass
                elif item["name"] == "door d" and dice_roll():
                    pass
                
                have_key = False
                for key in game_state["keys_collected"]:
                    if(key["target"] == item):
                        have_key = True
                if(have_key):
                    output += "You unlock it with a key you have."
                    next_room = get_next_room_of_door(item, current_room)
                else:
                    output += "It is locked but you don't have the key."

            # Handle furniture
            else:
                    if(item["name"] in object_relations and len(object_relations[item["name"]])>0):
                        # Piano interaction
                        if(item["name"] == "piano" and guessTheSongGame()):     # if the item is piano
                            item_found = object_relations[item["name"]].pop()
                            game_state["keys_collected"].append(item_found)
                            output += "You find " + item_found["name"] + "."
                        else:
                            item_found = object_relations[item["name"]].pop()
                            game_state["keys_collected"].append(item_found)
                            output += "You find " + item_found["name"] + "."
                    
                    # Couch interaction
                    elif item["name"] == "couch":
                        riddle = input("Solve this riddle to get the key (one word solution): 'I speak without a mouth and hear without ears. I have nobody, but I come alive with the wind. What am I?: \n").strip().lower()	
                        if riddle == "echo":
                            print("Correct! You can continue!\n")
                        else:
                            print("Wrong answer. You fall back asleep for 10 seconds.\n")
                            time.sleep(10)
                        play_room(current_room)
                        return
                    
                    # Other furniture interactions (bed, drawer, clock, etc.)
                    elif item["name"] == "queen bed":
                        riddle = input("Solve this riddle to get the key (one word solution): 'What gets bigger the more you take away?: \n'").strip().lower()
                        if riddle == "hole":
                            print("Correct! You found the key to the drawer!\n")
                            game_state["keys_collected"].append(key_drw)
                        else:
                            print("Wrong answer. You fall back asleep for 10 seconds.\n")
                            time.sleep(10)
                        play_room(current_room)
                        return
                    elif item["name"] == "drawer":
                        if key_drw in game_state["keys_collected"]:
                            print("You unlock the drawer with the key from the queen bed!\n")
                            print("You find the key to Door B inside the drawer!\n")
                            game_state["keys_collected"].append(key_b)
                        else:
                            print("The drawer is locked, and you don't have the key.\n")
                        play_room(current_room)
                        return
                    elif item["name"] == "alarm clock":
                        print("The alarm is ringing! You have 1 minute to guess the capital of France to turn it off.\n")
                        start_time = time.time()
                        time_limit = 60  # 1 minute limit
                        correct_guess = False
                        while not correct_guess and (time.time() - start_time) < time_limit:
                            guess = input("What is the capital of France?\n ").strip().lower()
                            if guess == "paris":
                                print("Correct! You turned off the alarm.\n")
                                correct_guess = True
                            else:
                                print("Wrong! Try again.\n")
                        if not correct_guess and (time.time() - start_time) >= time_limit:
                            print("Time's up! You failed to turn off the alarm and lost all your keys!\n")
                            game_state["keys_collected"] = []  # Lose all keys
                            game_state["current_room"] = game_room  # Send back to the game room
                            play_room(game_state["current_room"])  # Restart in the game room
                            return
                        elif correct_guess:
                            print("You managed to turn off the alarm in time!\n")
                        play_room(current_room)
                        return
                    
                    elif item["name"] == "double bed":
                        riddle = input("Solve this riddle to get the key (one word solution): 'What has a head and a tail, but no body?\n").strip().lower()
                        if riddle == "coin":
                            print("Correct! You found the key to door c!\n")
                            game_state["keys_collected"].append(key_c)
                        else:
                            print("Wrong answer. You fall back asleep for 10 seconds.\n")
                            time.sleep(10)
                        play_room(current_room)
                        return
                    elif item["name"] == "dresser":
                        print("The dresser is locked! To open it, you must win a game of rock-paper-scissors.\n")
                        rock_paper_scissors()
                        print("You won! You found the key to door b!")
                        game_state["keys_collected"].append(key_b)
                        play_room(current_room)
                        return
                    elif item["name"] == "table":
                        if quiz_game():
                            output += "You passed the quiz, but there's nothing else interesting here.\n"
                        else:
                            output += "There isn't anything interesting about it.\n"

                    print(output)
                    break

    if output is None:
        print("The item you requested is not found in the current room.\n")

    if next_room and input("Do you want to go to the next room? Enter 'yes' or 'no'\n").strip() == 'yes':
        play_room(next_room)
    else:
        play_room(current_room)



game_state = INIT_GAME_STATE.copy()

start_game()