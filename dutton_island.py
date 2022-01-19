# There's a bit of randomness in the game. Choosing the same path might
# result in more dialogue or may move you towards a scene with user choice.

import random
from os import system
from time import sleep
from sys import exit


# Validate input


def valid_input(prompt, options):
    while True:
        option = input(prompt).lower()
        if option in options:
            return option
        print_pause("Invalid option. Try again!")

# Print with pause: default 1 sec


def print_pause(text, time=1):
    print(text)
    sleep(time)


# Introduction
print_pause("\nWelcome to Dutton Island - A Choose Your Adventure Game by"
            " Gregory Brown", 3)
print_pause("Loading...............\n\n", 3)
print("Let me get some player information:\n\n")

# global variables
player = input("Please Enter Character Name: ")
lawyers_name = input("Give the name of your lawyer: ")
happy_words = input("What do you say when you're really happy?: ")
last_words = input("What would you like your last words to be?: ")
system('clear')

# GAME OPENING SEQUENCE - NOT REPEATABLE IF RESTARTED
print_pause("", 1)
print_pause("Loading................\n\n")
print("SCENE 1 - Dutton Island Prison - Visitor's Room\n")

# Opening Dialogue
print_pause(f"{lawyers_name}: Hey, {player} ! \n{lawyers_name}: "
            "I know you've been wrongfully imprisoned for 5 years on "
            "Dutton Island", 4)
print_pause(f"{player}: Listen {lawyers_name}, "
            "you know that I was framed.I'm losing my mind in here! "
            "How's the final appeal coming?", 2)
print_pause(f"{lawyers_name}: I'm sorry {player}, "
            "It looks like you will be executed in a week.", 3)
print_pause(f"{player}: What do you mean?", 4)
print_pause(f"{lawyers_name}: {player}, "
            "The system is corrupt and there's only a 1 % chance"
            " that they will even allow an appeal.", 5)
print_pause(f"{player}: So, {lawyers_name}, what choice do I have.", 3)
print_pause(f"{lawyers_name}: {player}, It's really risky. "
            "But, I think your only option is .......", 5)
print_pause(f"{lawyers_name}: Escape", 2)
print_pause(f"{player}: How?", 1)
print_pause(f"Guard: Visiting time is over!", 3)
print_pause(f"{lawyers_name}: Tomorrow, during your work placement. "
            "I've paid one of the guards to leave the door open.", 2)
print_pause("Once the way is clear. come closer. Take the.....", 4)
print_pause(f"Guard: That's it guys. Time's Up. {player}, "
            "back to your cell.\n", 3)
print_pause("END OF SCENE 1", 2)


print_pause("You didn't hear the end of the message. "
            "You'll just have to take your chances.\n", 3)


# END OF OPENING CUT SEQUENCE - GAMEPLAY STARTS AT ESCAPE DAY

def escape_day(player, lawyers_name):
    loading()
    print_pause("ESCAPE DAY\n", 2)
    print_pause(f"Guard: Hey {player}. {lawyers_name} "
                "paid me $1000 bucks to leave this door open.", 3)
    print_pause(f"Do whatever you want. But, if you get caught. "
                "I had nothing to do with this. Good luck!", 4)
    print_pause("The door is open and there is no one else around.\n", 3)

    escape_choice()


def escape_choice():
    """Give 4 options for player to choose escape path"""
    loading()
    print_pause("Where do you want to go?\n")
    print_pause("1: THE WOODS")
    print_pause("2: THE BRIDGE")
    print_pause("3: THE ROAD")
    print_pause("4: THE SHORELINE\n")

    choice = valid_input(
        'Enter the number. Then hit enter: ', [
            '1', '2', '3', '4'])

    if choice == '1':
        the_woods()
    elif choice == '2':
        the_bridge()
    elif choice == '3':
        the_road()
    else:
        the_shoreline()


def the_woods():
    """The woods escape storyline. The player spots hunters"""
    loading()
    print_pause("THE WOODS\n", 2)
    print_pause("You travelled all day and night.", 3)
    print_pause("You're now deep in the woods.", 3)
    print_pause("You find a small cave hidden away and decide to rest.", 3)
    print_pause("BANG!", 2)
    print_pause("You jolt awake at the sound. It's already dark. "
                "You must have slept most of the day.", 4)
    print_pause("A group of hunters have set up camp for the night. "
                "You've got some decisions to make.", 2)
    hunters()


def the_bridge():
    """The bridge escape storyline. One of four random_fate()
    will be chosen for the player"""
    loading()
    print_pause("THE BRIDGE\n")
    print_pause("You've arrived at the bridge")
    print_pause("You slowly get closer", 3)
    print_pause("Is the way clear?", 4)
    random_fate()


def the_road():
    """The road storyline. One of four
    random_fate() will be chosen for the player."""
    loading()
    print_pause("THE ROAD \n")
    print_pause("You've been walking on the road for the last 3 hours.", 3)
    print_pause("There has been very few cars. However, you'll dart "
                "into the bushes if you see one.", 3)
    print_pause("The road ahead is wide open with very few places to hide.", 3)
    print_pause("How will you fare?", 4)
    random_fate()


def the_shoreline():
    """The shoreline storyline. Player finds a canoe() and a raft()"""
    loading()
    print_pause("THE SHORELINE\n", 2)
    print_pause(
        "You arrive at the shoreline and you see a canoe and a raft.",
        3)
    print_pause("Which one do you choose?")
    print_pause("1: Canoe \n2: Raft")

    shoreChoice = valid_input('Enter 1 or 2: ', ['1', '2'])

    if shoreChoice == '1':
        sleep(2)
        canoe()
    else:
        sleep(2)
        raft()


def hunters():
    """Player runs into hunters"""
    loading()
    print_pause("THE HUNTERS\n", 2)
    print_pause("You've been hiding in this cave all night. "
                "The hunters aren't leaving anytime soon. ", 3)
    print_pause("You're hungry and thirsty. What do you do?", 3)
    hunters_choice()


def hunters_choice():
    """Decide to run back or approach hunters"""
    print_pause("")
    print_pause("Do you want to run or approach?")

    decisionWithHunters = valid_input('1: RUN \t2: APPROACH \n', ['1', '2'])

    if decisionWithHunters == '1':
        sleep(1)
        print_pause("You decide that the woods are too dangerous.")
        print_pause(
            "You wait until hunters are asleep and back "
            "track to choose a different path.")
        escape_choice()
    else:
        sleep(2)
        print_pause("You decide to approach the hunters.", 3)
        approach(player)


def approach(player):
    """Approach module, player has to decide to lie,
    confess, or bribe the hunters"""
    print_pause("THE APPROACH")
    print_pause("")
    approachGreeting = [
        'Hello there',
        'Wazz upppp',
        "What's happening home slice"]
    approachResponse = [
        'What do you want?',
        'Let me see your hands',
        'On your knees now.']

    approachChoices = {1: "Lie", 2: "Tell the Truth", 3: "Bribe"}

    # Quick random fun dialogue
    print(f"{player}: ", random.choice(approachGreeting))
    print("Hunters: ", random.choice(approachResponse))
    sleep(2.5)
    print_pause("")

    print_pause(approachChoices, 5)
    howToApproach = valid_input(
        'How do you respond, 1,2 or 3 \n', [
            '1', '2', '3'])

    if howToApproach == '1':
        lie(player)
    elif howToApproach == '2':
        confess()
    else:
        bribe()


def lie(player):
    """If player decides to lie, the game calls random_lie to decide fate"""
    loading()
    print_pause("You CHOSE TO LIE:\n", 2)

    liesToTell = {
        1: "I'm just a fellow hunter who got lost in the woods.",
        2: "I came to the island on a day trip.",
        3: "I'm a geologist, I'm just collecting rocks."}

    for lieKey, lieValue in liesToTell.items():
        print(f"{lieKey}: {lieValue}")

    print_pause("", 2)
    print_pause("What lie do you want to tell?")

    theLieToUse = valid_input(
        "What lie do you want to tell? 1,2 or 3 \n", ['1', '2', '3'])
    print_pause("")
    print(f"{player}: ", liesToTell.get(theLieToUse))
    sleep(3.4)

    if theLieToUse == '1':
        print_pause("Hunters: We don't believe you. "
                    "We heard about your escape. Jim, Grab him!", 5)
        death_in_woods(last_words)
    else:
        print_pause("Hunters: That sounds reasonable. How can we help?\n", 4)
        print_pause(f"{player}: Take me to the shoreline.", 4)
        the_shoreline()


def death_in_woods(last_words):
    """Player dies - repurposed for any death"""
    loading()
    print_pause("Everything goes dark.", 2)
    print_pause("You are alone", 2)
    print_pause("You feel a warm liquid pouring down your face.", 3)
    print_pause("You must have been hit in the head.", 3)
    print_pause("You try to move. But you can't", 3)
    print_pause("You realize that this is it. This is how it ends.", 3)
    print_pause("You close your eyes and whisper: ", 3)
    print_pause(f"{last_words}", 4)
    system('clear')
    sleep(2)
    credits()


def confess():
    """Scene where player confesses that they are escaped con.
    Will call random_confess() to decide
    players fate"""
    loading()
    print_pause("YOU DECIDE TO CONFESS\n")

    confesseeDict = {
        1: 'The person giving you the death stare',
        2: 'The person with the eye patch',
        3: 'The fellow in the corner'}

    # print out consessee options
    for confesseeKey, confesseeVal in confesseeDict.items():
        print_pause(f"{confesseeKey}: {confesseeVal}\n")

    confessTo = valid_input(
        "Who do you want to confess to: 1,2 or 3 \n", ['1', '2', '3'])
    sleep(2)

    # The choice of who to confess to must match the random decider
    if confessTo == '1':
        print_pause(" Sorry, you chose the wrong person to confess to.", 3)
        death_in_woods(last_words)
    elif confessTo == '2':
        print_pause("Thanks for being honest. "
                    "We will help you get to The Bridge.", 4)
        the_bridge()
    else:
        print_pause(
            "We are a religous cult and like honesty. "
            "We will escort you to The Road.", 4)
        the_road()

# Bribe scene


def bribe():
    """Player decides to bribe hunters and
    players fate is chosen by random draw of either
    death_in_woods or player is allowed to go to the_road()"""
    loading()
    print_pause("YOU DECIDE TO BRIBE THE HUNTERS\n", 2)

    bribeWithDict = {
        1: 'Pack of Cigarettes',
        2: 'Your Boots',
        3: 'The Watch You Took With You'}

    # print out bribe options
    for bribeKey, bribeVal in bribeWithDict.items():
        print_pause(f"{bribeKey}: {bribeVal}\n")

    bribeThemWith = valid_input(
        "What do you want to use to bribe them: 1,2 or 3\n", ['1', '2', '3'])
    sleep(2)

    if bribeThemWith == '1':
        print_pause(" Sorry, you chose the wrong bribe.", 3)
        death_in_woods(last_words)
    else:
        print_pause("Thanks for that.", 4)
        print_pause("We'll help you get to The Road.")
        the_road()

# Randomizer for different scenes


def random_fate():
    """This module is shared by the_bridge()
    and the_road(). It randomly chooses between
    4 different scenarios:
    roadblock(), vehicle(), chopper(), or all_clear()."""
    fateRandom = random.randint(1, 5)

    if fateRandom == 1:
        roadblock()
    elif fateRandom == 2:
        vehicle()
    elif fateRandom == 3:
        all_clear()
    elif fateRandom == 4:
        chopper()
    elif fateRandom == 5:
        all_clear()

# Roadblock scene


def roadblock():
    """Player runs into a road block. It's the end of the line.
    Player will either be shot() or captured()."""
    loading()
    roadBlockFate = random.randint(1, 2)
    print_pause("ROAD BLOCK AHEAD")
    print_pause("")
    print_pause("There is a road block ahead", 3)
    print_pause("There is nowhere to run or hide.", 3)

    if roadBlockFate == 1:
        shot(last_words)
    else:
        captured()
# Player last words


def shot(last_words):
    """Player is shot"""
    loading()
    print_pause("BANG!", 2)
    print_pause("As you approach, they start shooting.", 2)
    print_pause("BANG! BANG!", 3)
    print_pause("You shout. I'm unarmed. I surrender!", 3)
    print_pause("BANG! BANG! BANG!", 4)
    print_pause(
        "It's too late. You clutch your side and fall to the ground.",
        4)
    print_pause("Eveything is quiet now.", 4)
    print_pause("As you look to the sky and your eyes slowly close. "
                "You whisper: ", 4)
    print_pause(f"{last_words}", 6)
    credits()

# Player is captured


def captured():
    """Player is captured"""
    loading()
    print_pause("THE END OF THE LINE\n")
    print_pause("Get down on the ground now.", 3)
    print_pause("You are surrounded", 2)
    print_pause("You are recaptured", 4)
    recaptured()

# Vehicle approaching scene


def vehicle():
    """Player encounters a vehicle and random_vehicle()
    module is called to determine fate."""
    loading()
    vehicleDecider = random.randint(1, 2)
    print_pause("VEHICLE AHEAD\n", 3)
    print_pause("There is a vehicle approaching ahead. "
                "They have seen you. There is nowhere to hide", 4)

    if vehicleDecider == 1:
        print_pause("You start to run. But you see that there is "
                    "a car behind and a roadblock ahead.", 3)
        roadblock()
    else:
        print_pause("As the car approaches, "
                    "you notice that it is the security guard.", 3)
        print_pause(
            "He's reluctant. But, he decides to take you to the shoreline.", 3)
        the_shoreline()

# Chopper overhead scene


def chopper():
    """A chopper starts flying overhead."""
    loading()
    print_pause("HELICOPTER OVERHEAD\n", 3)
    print_pause("There is a chopper overhead. Do you run left or right?", 3)

    chopperChoice = valid_input("1. Left    2. Right: [1|2] \n", ['1', '2'])

    if chopperChoice == '1':
        print_pause("You start running back towards the woods", 4)
        hunters()
    else:
        print_pause("They chase you towards the roadblock", 3)
        roadblock()

# All clear module


def all_clear():
    """All is clear for player.  module calls shoreline()"""
    loading()
    print_pause(f"You slowly decide to approach.", 3)
    print_pause(f"There are vehicles passing.", 3)
    print_pause("You decide to hide until nightfall.", 4)
    print_pause(
        f"Its dark now. You haven't seen any "
        "movement for the last 2 hours.", 4)
    print_pause(
        f"You decide that your best move now "
        "is to go to the shoreline.", 2)
    the_shoreline()

# The canoe scene


def canoe():
    """Part of the shoreline() storyline.
    Player chooses canoe.
    And, then has a choice of going south() or north()"""
    loading()
    print_pause("You chose the canoe.")
    print_pause("")
    print_pause("Do you want to go: \n1: North \n2: South\n")

    canoeChoice = valid_input("Enter 1 or 2: ", ['1', '2'])

    if canoeChoice == '1':
        print_pause("You chose to go north", 2)
        run_rapids()
    else:
        print_pause("You're going south", 2)
        rapids()

# The raft title scene


def raft():
    """Part of the shoreline() storyline. Player chooses raft. """
    loading()
    print_pause("RAFTING\n")
    print_pause("While rafting you come upon some rapids "
                "and you have no choice but to run them.", 4)
    run_rapids()

# The rapids title screen


def rapids():
    """Player sees rapids ahead"""
    loading()
    print_pause("You see rapids ahead. But you vessel is sturdy enough\n", 4)
    other_side()

# The running the rapids scene


def run_rapids():
    """Player decides to run the rapids.
    If a random number between 1 and 3, player collapse() and dies,
    else reach other_side()."""
    loading()
    rapidsClassRandom = random.randint(1, 6)
    print_pause("If the rapid is a class 5 or 6 - you will not survive.", 2)
    print_pause("Calculating rapid class...................\n", 5)
    print_pause(f"This is a class {rapidsClassRandom} rapid")

    if rapidsClassRandom != 5 or rapidsClassRandom != 6:
        print_pause("Awesome Sauce!", 3)
        other_side()
    else:
        print_pause("I'm so sorry", 3)
        death_in_woods(last_words)

# The scene if the player reaches the other side


def other_side():
    """Player reaches the other side of river
    to a town and see's a payphone()."""
    loading()
    print_pause("You've reached to the other side. "
                "You are now on the mainland")
    print_pause("I ran out of ideas. You have one last random "
                "challenge that's completly unrelated to storyline..", 4)
    print_pause("Im thinking of a number between 1 and 10.")
    print_pause("If not. You will be recaptured and your sentencing "
                "will be handed down.", 3)

    playerGuessInput = valid_input(
        "What number do you guess:  1 to 10: ", [
            '1', '2', '3', '4', '5', '6', '7', '8', '9', '10'])
    playerGuess = int(playerGuessInput)

    randomLastChance = random.randint(1, 10)

    winNum1 = randomLastChance
    winNum2 = randomLastChance + 2
    winNum3 = randomLastChance - 2

    if (playerGuess == winNum1 or playerGuess == winNum2
            or playerGuess == winNum3):
        sleep(4)
        print_pause(f"You guessed {playerGuess}", 2)
        print("The number that I thought of is:", end=' ')
        sleep(6)
        print_pause(randomLastChance, 2)
        print_pause("Congrats", 2)
        win(player)
    else:
        sleep(4)
        print_pause(f"You guessed {playerGuess}", 2)
        print("The number that I thought of is:", end=' ')
        sleep(6)
        print_pause(randomLastChance, 2)
        print_pause("I'm so sorry.", 2)
        recaptured()

# What happens if the player wins


def win(player):
    """Winning module"""
    loading()
    print_pause("")

    # Credit for border code: user: 8121077 on stackoverflow.com
    def border_msg(msg):
        msg_lines = msg.split('\n')
        max_length = max([len(line) for line in msg_lines])
        count = max_length + 2

        dash = "*" * count

        print("*%s*" % dash)

        for line in msg_lines:
            half_dif = (max_length - len(line))
            if half_dif == 0:
                print("* %s *" % line)
            else:
                print("* %s " % line + ' ' * half_dif + '*')

        print("*%s*" % dash)
    sleep(3)
    border_msg(
        f"Congratulations {player}\nYou Have Escaped Dutton Island\n "
        "You Are The Best!\n"
        "Thanks for playing")
    sleep(5)
    credits()

# What happens if player is recaptured


def recaptured():
    """Player is recaptured. A random choice is made whether:
    death penalty, life, or 15 yrs with paraole in 5."""
    loading()
    print_pause("Back to jail for you")
    randomSentencing = random.randint(1, 6)

    if (randomSentencing == 1 or randomSentencing == 3
            or randomSentencing == 6):
        sleep(2)
        parole()
    elif randomSentencing == 2 or randomSentencing == 4:
        sleep(2)
        life(player)
    else:
        sleep(2)
        death_penalty()

# The death penalty option


def death_penalty():
    """Death penalty ending storyline"""
    loading()
    print_pause("")
    print_pause("There will be no mercy.")
    print_pause("You have been sentenced to death by tickling squad.")
    print_pause("May Tiger King have mercy on your soul.", 3)
    credits()

# The life sentence option


def life(player):
    """Life imprisonment ending storyline."""
    loading()
    print_pause("")
    print_pause("The Judge is deliberating.....", 2)
    print_pause(f"{player}, you have been sentenced to life in prison "
                "without possibility of parole.", 3)
    credits()

# The parole sentence option


def parole():
    """15 years with parole after 5 years storyline."""
    loading()
    print_pause("")
    print_pause("The judge is deliberating......", 2)
    print_pause("The court will be lenient in these matters.")
    print_pause(
        "I sentence you to 15 years in prison. "
        "However, if you are a model prisoner, you'll be out in 5 years", 3)
    credits()


def credits():
    print_pause(" Thanks for playing!")


def loading():
    print_pause("Loading................")
    system('clear')
    sleep(1)


def play_game(player, lawyers_name):
    while True:
        escape_day(player, lawyers_name)
        break


def play_again():
    choice = valid_input("Would you like to play again? [y|n]: ", ['y', 'n'])
    if choice == 'n':
        credits()
        exit(0)


def game(player, lawyers_name):
    while True:
        play_game(player, lawyers_name)

        play_again()


if __name__ == '__main__':
    game(player, lawyers_name)
