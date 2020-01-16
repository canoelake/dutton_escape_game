import random
from os import system
from time import sleep
from sys import exit
# player ="test player"
# crime = "test crime"
# lawyers_name ="Test lawyer"
# happy_words = "I am happy"
# last_words = "This is my last word"

sleep(1)
print("")
print("Welcome to Dutton Island - A Choose Your Adventure Game by Gregory Brown")
sleep(2)
print("Loading...............")
sleep(3)
print("")
print("")
print("Let me get some player information:")
print("")
print("")
player = input("Please Enter Character Name: ")
crime = input("Name a crime: ")
lawyers_name = input("Give the name of your lawyer: ")
happy_words = input("What do you say when you're really happy?: ")
last_words = input("What would you like your last words to be?: ") #Players last words
print("Loading...............")
sleep(1.2)
system('clear')

def welcome(player, lawyers_name):
    """Game welcome screen"""
    #Game Loading Screen
    print("")
    sleep(3)
    print("Loading................")
    sleep(3)
    print("")
    print("")
    print("SCENE 1 - Dutton Island Prison - Visitor's Room")
    print("")

    #Opening Dialogue
    print(f"{lawyers_name}: Hey, {player} ! \n{lawyers_name}: I know you've been wrongfully imprisoned for 5 years on Dutton Island")
    sleep(4)
    print(f"{player}: Listen {lawyers_name}, you know that I was framed. I'm losing my mind in here! How's the final appeal coming?")
    print(f"{lawyers_name}: I'm sorry {player}, It looks like you will be executed in a week.")
    sleep(3)
    print(f"{player}: What do you mean?")
    sleep(4)
    print(f"{lawyers_name}: {player}, The system is corrupt and there's only a 1 % chance that they will even allow an appeal.")
    sleep(5)
    print(f"{player}: So, {lawyers_name}, what choice do I have.")
    sleep(3)
    print(f"{lawyers_name}: {player}, It's really risky. But, I think your only option is .......")
    sleep(5)
    print(f"{lawyers_name}: Escape")
    sleep(1)
    print(f"{player}: How?")
    sleep(1.5)
    print(f"Guard: Visiting time is over!")
    sleep(3)
    print(f"{lawyers_name}: Tomorrow, during your work placement. I've paid one of the guards to leave the door open.")
    print("Once the way is clear. come closer. Take the.....")
    sleep(5.2)
    print(f"Guard: That's it guys. Time's Up. {player}, back to your cell.")
    print("")
    print("END OF SCENE 1")
    
    #Option to continue game or to exit
    sleep(6)
    system('clear')
    print("")
    print("Even though you didn't hear the end of the message. Do you risk it? Or, will you stay and probably be executed?")
    print("")
    

    # checks for user input if they want to proceed
    proceed = input("Do you want to proceed? ")
    if proceed == "Y" or proceed == "y":
        print(f"Good Luck {player}!")
        sleep(1.2)
        print("Loading...............")
        sleep(2)
        escape_day(player, lawyers_name)
    elif proceed == "N" or proceed == "n":
        print("I'm not sure sure you made the right choice!")
        sleep(3)
        recaptured()
    else:
        print("Invalid Entry. Exiting.")
        sleep(1)
        exit()

def escape_day(player, lawyers_name):
    loading()
    print("ESCAPE DAY")
    print("")
    sleep(2)
    print(f"Guard: Hey {player}. {lawyers_name} paid me $1000 bucks to leave this door open.")
    sleep(3)
    print(f"Do whatever you want. But, if you get caught. I had nothing to do with this. Good luck!")
    sleep(3)
    loading()
    print("The door is open and there is no one else around.")
    sleep(3)
    print("It looks like there are 4 paths that you could take.")
    print("1: THE WOODS")
    print("2: THE BRIDGE")
    print("3: THE ROAD")
    print("4: THE SHORELINE")
    sleep(5)
    escape_choice(player, lawyers_name)

def escape_choice(player, lawyers_name):
    """Give 4 options for player to choose escape path"""
    loading()
    print("Where do you want to go?")
    print("")
    sleep(2)
    print("1: THE WOODS")
    sleep(2)
    print("2: THE BRIDGE")
    sleep(2)
    print("3: THE ROAD")
    sleep(2)
    print("4: THE SHORELINE")

    print("")

    choice = int(input('Write the number of your choice. Then hit enter: '))

    if choice == 1 :
        the_woods()
    elif choice == 2 :
        the_bridge()
    elif choice == 3 :
        the_road()
    elif choice == 4:
        the_shoreline
    else:
        print("Sleep it off and try again later")
        sleep(3)
        credits()
    
def the_woods():
    """The woods escape storyline. The player spots hunters"""
    loading()
    location = "the woods"
    print("THE WOODS")
    print("")
    sleep(2)
    print("You travelled all day and all night.")
    sleep(2.5)
    print("You're now deep in the woods.")
    sleep(2.5)
    print("You find a small cave hidden away and decide to rest.")
    sleep(4)
    print("BANG!")
    sleep(2.5)
    print("You jolt awake at the sound. It's already dark. You must have slept most of the day.")
    sleep(4)
    print("A group of hunters have set up camp for the night. You've got some decisions to make.")
    
    hunters()

def the_bridge(player):
    """The bridge escape storyline. One of four random_fate() will be chosen for the player"""
    loading()
    location = "the bridge"
    print("THE BRIDGE")
    print("")
    sleep(1)
    print("You've arrived at the bridge")
    sleep(1.3)
    print("You slowly get closer")
    sleep(3)
    print("Is the way clear?")
    sleep(3.5)
    random_fate()

def the_road(player):
    """The road storyline. One of four random_fate() will be chosen for the player."""
    loading()
    location = "the road"
    print("THE ROAD")
    print("")
    sleep(1)
    print("You've been walking on the road for the last 3 hours.")
    sleep(3)
    print("There has been very few cars. However, you'll dart into the bushes if you see one.")
    sleep(3)
    print("The road ahead is wide open with very few places to hide.")
    sleep(3)
    print("How will you fare?")
    sleep(4)
    random_fate()

def the_shoreline(player):
    """The shoreline storyline. Player finds a canoe() and a raft()"""
    loading()
    location = "the shoreline"
    print("THE SHORELINE")
    print("")
    sleep(2)
    print("You arrive at the shoreline and you see a conoe and a raft.")
    sleep(3)
    
    print("Which one do you choose?")
    print("1: Canoe \n2: Raft")
    sleep(1)
    shoreChoice = int(input('Enter 1 or 2: '))

    if shoreChoice != 1 or shoreChoice ! = 2:
        print('Read the instructions.')
        print('Reloading.............')
        sleep(2)
        the_shoreline(player)
    elif shoreChoice == 1:
        sleep(2)
        canoe()
    elif shoreChoice == 2:
        sleep(2)
        raft()
    else:
        print("Exiting Game")
        sleep(0.8)
        credits()
    
def hunters():
    """Player runs into hunters"""
    loading()
    location = "the hunters"
    print("THE HUNTERS")
    print("")
    sleep(2)
    print("You've been holed up in this cave all night. The hunters aren't leaving anytime soon. ")
    sleep(3)
    print("You're hungry and thirsty. What do you do?")
    sleep(5)
    hunters_choice()
    
def hunters_choice():
    """Decide to run back or approach hunters"""
    loading()
    print("")
    print("Do you want to run or approach?")
    sleep(1)
    print("1: RUN \t\t2: APPROACH")

    decisionWithHunters = int(input('> '))

    if decisionWithHunters == 1:
        sleep(1)
        print("You decide that the woods are too dangerous.")
        sleep(1)
        print("You wait until hunters are asleep and back track to choose a different path.")
        escape_choice(player, lawyers_name)
    elif decisionWithHunters == 2:
        sleep(1)
        print("You decide to approach the hunters.")
        sleep(3)
        approach(player)
    else:
        hunters()

def approach(player):
    """Approach module, player has to decide to lie, confess, or bribe the hunters"""
    loading()
    print("THE APPROACH")
    print("")
    approachGreeting = ['Hello there', 'Wazz upppp', "What's happening home slice"]
    approachResponse = ['What do you want?', 'Let me see your hands', 'On your knees now.']

    approachChoices = {1:"Lie", 2:"Tell the Truth", 3:"Bribe"}

    print(f"{player}: ", random.choice(approachGreeting))
    sleep(2.5)
    print("Hunters: ", random.choice(approachResponse))
    sleep(2.5)
    print("")
    print("How do you respond?")
    sleep(2.5)
    print("")

    print(approachChoices)
    print("")
    howToApproach = int(input('> '))
    sleep(5)

    if howToApproach in approachChoices:
        print("You chose to :", end=' ')
        print(approachChoices.get(howToApproach))
    else:
        print("Incorrect selection")
        approach(player)
    
    if howToApproach == 1:
        lie(player)
    elif howToApproach == 2:
        confess(player)
    elif howToApproach == 3:
        bribe(player)
    else:
        print("Forget it.")
        sleep(2)
        credits()


def lie(player):
    """If player decides to lie, the game calls random_lie to decide fate"""
    loading()
    print("You CHOSE TO LIE:")
    print("")
    sleep(2)

    liesToTell = {1:"I'm just a fellow hunter who got lost in the woods.",
    2: "I came to the island on a day trip.", 3:"I'm a geologist, I'm just collecting rocks."}

    lieDetector = random.randint(1,3)

    for lieKey, lieValue in liesToTell.items():
        print(f"{lieKey}: {lieValue}")
    
    print("")
    sleep(2)
    print("What lie do you want to tell?")

    theLieToUse = int(input('> '))
    print("")
    print(f"{player}: ", liesToTell.get(theLieToUse))
    sleep(3.4)

    if theLieToUse != lieDetector:
        print("Hunters: We don't believe you. We heard about your escape. Jim, Grab him!")
        sleep(5)
        lie(player)
        death_in_woods(last_words)
    elif theLieToUse == lieDetector:
        print("Hunters: That sounds reasonable. How can we help?")
        print("")
        sleep(3.6)
        print(f"{player}: Take me to the shoreline.")
        sleep(4)
        the_shoreline(player)
    else:
        print("Come on man. Please read instructions.")
        sleep(2)
        lie(player)

def death_in_woods(last_words):
    """Player dies - repurposed for any death"""
    loading()
    print("Everything goes dark.")
    sleep(2)
    print("You are alone")
    sleep(2)
    print("You feel a warm liquid pouring down your face.")
    sleep(2.5)
    print("You must have been hit in the head.")
    sleep(2.9)
    print("You try to move. But you can't")
    sleep(2.5)
    print("You realize that this is it. This is how it ends.")
    sleep(2.6)
    print("You close your eyes and whisper: ")
    sleep(3.5)
    print(f"{last_words}")
    sleep(4.3)
    system('clear')
    sleep(1)
    credits()

def confess(player):
    """Scene where player confesses that they are escaped con. Will call random_confess() to decide
    players fate"""
    loading()
    print("YOU DECIDE TO CONFESS")
    print("")
    sleep(1)

    confesseeDict = {1:'Joe', 2:'The Bearded Woman', 3:'The Ugly Fellow in the corner'}
    confessDecider = random.randint(1,3)
    randomConfessPath = random.randint(1,2)
    
    for confesseeKey, confesseeVal in confesseeDict.items():
        print(f"{confesseeKey}: {confesseeVal}")
        print("")

    confessTo = int(input("Who do you want to confess to: "))
    sleep(1.2)

    print("You choose to confess to ", confesseeDict.get(confessTo))
    sleep(3)

    if confessTo != confessDecider:
        print(" Sorry, you chose the wrong person to confess to.")
        sleep(3)
        death_in_woods(last_words)
    elif randomConfessPath == 1:
        print("Thanks for being honest. We will help you get to The Bridge.")
        sleep(6)
        the_bridge(player)
    elif randomConfessPath == 2:
        print("We are a crazy religous cult and like honesty. We will excort you to The Road.")
        sleep(6)
        the_road(player)
    else:
        print("You can't take instructions.")
        sleep(1)
        credits()
    

def bribe(player):
    """Player decides to bribe hunters and players fate is chosen by random draw of either
    death_in_woods or player is allowed to go to the_road()"""
    loading()
    print("YOU DECIDE TO BRIBE THE HUNTERS")
    print("")
    sleep(1)

    bribeWithDict = {1:'Pack of Cigarettes', 2:'Your Boots', 3:'The Watch You Took With You'}
    bribeDecider = random.randint(1,3)
        
    for bribeKey, bribeVal in bribeWithDict.items():
        print(f"{bribeKey}: {bribeVal}")
        print("")

    bribeThemWith = int(input("What do you want to use to bribe them: "))
    sleep(1.2)

    print("You choose to bribe them with ", bribeWithDict.get(bribeThemWith))
    sleep(3)

    if bribeThemWith != bribeDecider:
        print(" Sorry, you chose the wrong bribe.")
        sleep(3)
        death_in_woods(last_words)
    else:
        print("Thanks for ", bribeWithDict.get(bribeThemWith))
        sleep(4)
        print("We'll help you get to The Road.")
        the_road(player)


def random_fate():
    """This module is shared by the_bridge() and the_road(). It randomly chooses between 4 different scenarios:
    roadblock(), vehicle(), chopper(), or all_clear()."""
    fateRandom = random.randint(1,5)
    location = "the bridge via the road"
    
    if fateRandom == 1:
        roadblock()
    elif fateRandom == 2:
        vehicle()
    elif fateRandom == 3:
        all_clear(location)
    elif fateRandom == 4:
        chopper()
    elif fateRandom == 5:
        all_clear(location)
    else:
        print("This is too hard. Quitting.")
        sleep(2)
        credits()

def roadblock():
    """Player runs into a road block. It's the end of the line. Player will either be shot() or captured()."""
    loading()
    roadBlockFate = random.randint(1,2)
    print("ROAD BLOCK AHEAD")
    print("")
    print("There is a road block ahead")
    sleep(3)
    print("There is nowhere to run or hide.")
    sleep(3)

    if roadBlockFate == 1:
        shot(last_words)
    else:
        captured()

def shot(last_words):
    """Player is shot"""
    loading()
    print("BANG!")
    sleep(2)
    print("As you approach, they start shooting.")
    sleep(2)
    print("BANG! BANG!")
    sleep(3)
    print("You shout. I'm unarmed. I surrender!")
    sleep(3)
    print("BANG! BANG! BANG!")
    sleep(4)
    print("It's too late. You clutch your side and fall to the ground.")
    sleep(6)
    print("Eveything is quiet now.")
    sleep(4)
    print("As you look to the sky and your eyes slowly close. You whisper: ")
    sleep(4)
    print(f"{last_words}")
    sleep(6)
    credits()

def captured():
    """Player is captured"""
    loading()
    print("THE END OF THE LINE")
    print("")
    print("Get down on the ground now.")
    sleep(3)
    print("You are surrounded")
    sleep(2)
    print("You are recaptured")
    sleep(4)
    recaptured()

def vehicle():
    """Player encounters a vehicle and random_vehicle() module is called to determine fate."""
    loading()
    vehicleDecider = random.randint(1,2)
    print("VEHICLE AHEAD")
    print("")
    sleep(3)
    print("There is a vehicle approaching ahead. They have seen you. There is nowhere to hide")
    sleep(5)
    
    if vehicleDecider == 1:
        print("You start to run. But you see that there is a car behind and a roadblock ahead.")
        sleep(4)
        roadblock()
    else:
        print("As the car approaches, you notice that it is the security guard.")
        sleep(3)
        print("He's reluctant. But, he decides to take you to the shoreline.")
        sleep(5)
        the_shoreline(player)

def chopper():
    """A chopper starts flying overhead."""
    loading()
    print("HELICOPTER OVERHEAD")
    print("")
    sleep(3)
    print("There is a chopper overhead. Do you run left or right?)
    sleep(3)
    
    chopperDecider = random.randint(1,2)
    chopperChoice = int(input("1. Left    2. Right: "))

    if chopperChoice == chopperDecider:
        print("You start running back towards the woods")
        sleep(4)
        hunters()
    else:
        print("They chase you towards the roadblock")
        sleep(3)
        roadblock()
    

def all_clear(location):
    """All is clear for player.  module calls shoreline()"""
    loading()
    print(f"You slowly decide to approach {location}.")
    sleep(3)
    print(f"There are vehicles on {location}.")
    sleep(3)
    print("You decide to hide until nightfall.")
    sleep(4)
    print(f"Its dark now. You haven't seen any movement on {location} for the last 2 hours.")
    sleep(4)
    print(f"You decide that your best move now is to follow {location} to the shoreline.")
    sleep(2)

def canoe():
    """Part of the shoreline() storyline. Player chooses canoe. And, then has a choice of going south() or north()"""
    loading()
    print("You chose the canoe.")
    print("")
    print("Do you want to go: \n1: North \n2: South\n")
    
    canoeChoice = int(input("Enter 1 or 2: "))

    if canoeChoice != 1 or canoeChoice != 2:
        print("Incorrect choice")
        sleep(1)
        canoe()
    elif canoeChoice == 1:
        print("You chose to go north")
        sleep(2)
        run_rapids()
    elif canoeChoice == 2:
        print("You're going south")
        sleep(2)
        rapids()
    else:
        print("Bug in the system")
        sleep(1)
        credits()
    

def raft():
    """Part of the shoreline() storyline. Player chooses raft. """
    loading()
    print("RAFTING")
    print("")
    sleep(1)
    print("While rafting you come upon some rapids and you have no choice but to run them.")
    sleep(4)
    run_rapids()

def rapids():
    """Player sees rapids ahead"""
    loading()
    print("You see rapids ahead. But you vessel is sturdy enough")
    print("")
    sleep(3.4)
    other_side()


def run_rapids():
    """Player decides to run the rapids. If a random number between 1 and 3, player collapse() and dies, 
    else reach other_side()."""
    loading()
    rapidsClassRandom = random.randint(1,6)
    print("If the rapid is a class 5 or 6 - you will not survive.")
    sleep(2)
    print("Calculating rapid class...................")
    sleep(5)
    print("")
    print(f"This is a class {rapidsClassRandom} rapid")

    if rapidsClassRandom != 5 or rapidsClassRandom != 6:
        print("Great")
        sleep(3)
        other_side()
    else:
        print("I'm so sorry")
        sleep(3)
        death_in_woods(last_words)
   

def other_side():
    """Player reaches the other side of river to a town and see's a payphone()."""
def payphone():
    """Player get's in payphone and must complete last_boss() to win."""
def last_boss():
    """Player has 3 chances to complete challenge to win() or be recaptured()."""
def win(player):
    """Winning module"""
    loading()
    print("")
    
    def border_msg(msg):
        msg_lines=msg.split('\n')
        max_length=max([len(line) for line in msg_lines])
        count = max_length +2 

        dash = "*"*count 

        print("*%s*" %dash)

        for line in msg_lines:
            half_dif=(max_length-len(line))
            if half_dif==0:
                print("* %s *"%line)
            else:
                print("* %s "%line+' '*half_dif+'*')    

        print("*%s*"%dash)
    sleep(3)
    border_msg(f'Congratulations {player}\nYou Have Escaped Dutton Island\n You Are The Best!')
    sleep(5)
    credits()

def recaptured():
    """Player is recaptured. A random choice is made whether: death penalty, life, or 15 yrs with paraole in 5."""
    print("This is recaptured")
def death_penalty():
    """Death penalty ending storyline"""
    loading()
    print("")
    print("There will be no mercy.")
    print("You have been sentenced to death by firing squad.")
    sleep(1)
    print("May Darwin have mercy on your soul.")
    sleep(3)
    credits()

def life(player):
    """Life imprisonment ending storyline."""
    loading()
    print("")
    print("The Judge is deliberating.....")
    sleep(1.2)
    print(f"{player}, you have been sentenced to life in prison without possibility of parole.")
    sleep(3)
    credits()

def parole():
    """15 years with parole after 5 years storyline."""
    loading()
    print("")
    print("The judge is deliberating......")
    sleep(1.5)
    print("The court will be lenient in these matters.")
    sleep(0.5)
    print("I sentence you to 15 years in prison. However, if you are a model prisoner, you'll be out in 5 years")
    sleep(3)
    credits()


def credits():
    print("")
    print("Escape from Dutton Island")
    print("Concept and coding by Gregory Brown")
    print("Created to demonstrate beginner level competency in Python")
    print("January 2020")
def loading():
    print("Loading................")
    sleep(1.5)
    system('clear')
    sleep(2)


welcome(player, lawyers_name)

