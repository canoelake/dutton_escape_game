import time
from sys import exit

time.sleep(1)
print("")
print("Welcome to Dutton Island - A Choose Your Adventure Game by Gregory Brown")
time.sleep(2)
print("Loading...............")
time.sleep(3)
print("")
print("")
print("Let me get some player information:")
print("")
print("")
player = input("Please Enter Character Name: ")
crime = input("Name a crime: ")
lawyers_name = input("Give the name of your lawyer: ")
happy_words = input("What do you say when you're really happy?: ")
last_words = input("What would you like your last words to be?: ")


def welcome(player, lawyers_name):
    """Game welcome screen"""
    #Game Loading Screen
    print("")
    time.sleep(3)
    print("Loading................")
    time.sleep(3)
    print("")
    print("")
    print("SCENE 1 - Dutton Island Prison - Visitor's Room")
    print("")

    #Opening Dialogue
    print(f"{lawyers_name}: Hey, {player} ! \n{lawyers_name}: I know you've been wrongfully imprisoned for 5 years on Dutton Island")
    time.sleep(4)
    print(f"{player}: Listen {lawyers_name}, you know that I was framed. I'm losing my mind in here! How's the final appeal coming?")
    print(f"{lawyers_name}: I'm sorry {player}, It looks like you will be executed in a week.")
    time.sleep(4)
    print(f"{player}: What do you mean?")
    time.sleep(4)
    print(f"{lawyers_name}: {player}, The system is corrupt and there's only a 1 % chance that they will even allow an appeal.")
    time.sleep(5)
    print(f"{player}: So, {lawyers_name}, what choice do I have.")
    time.sleep(3)
    print(f"{lawyers_name}: {player}, It's really risky. But, I think your only option is .......")
    time.sleep(5)
    print(f"{lawyers_name}: Escape")
    time.sleep(1)
    print(f"{player}: How?")
    time.sleep(1.5)
    print(f"Guard: Visiting time is over!")
    time.sleep(3)
    print(f"{lawyers_name}: Tomorrow, during your work placement. I've paid one of the guards to leave the door open.")
    print("Once the way is clear. come closer. Take the.....")
    time.sleep(5)
    print(f"Guard: That's it guys. Time's Up. {player}, back to your cell.")
    print("")
    print("END OF SCENE 1")
    
    #Option to continue game or to exit
    time.sleep(6)
    print("")
    print("Even though you didn't hear the end of the message. Do you risk it? Or, will you stay and probably be executed?")
    print("")
    

    # checks for user input if they want to proceed
    proceed = input("Do you want to proceed? ")
    if proceed == "Y" or proceed == "y":
        print(f"Good Luck {player}!")
        time.sleep(1)
        print("Loading...............")
        time.sleep(2)
        escape_choice()
    elif proceed == "N" or proceed == "n":
        print("I'm nto sure sure you made the right choice!")
        time.sleep(3)
        recaptured()
    else:
        print("Invalid Entry. Exiting.")
        time.sleep(1)
        exit()

def escape_choice():
    """Give 4 options for player to choose escape path"""
    print("choice")
def the_woods():
    """The woods escape storyline. The player spots hunters"""
def the_bridge():
    """The bridge escape storyline. One of four random_fate() will be chosen for the player"""
def the_road():
    """The road storyline. One of four random_fate() will be chosen for the player."""
def the_shoreline():
    """The shoreline storyline. Player finds a canoe() and a raft()"""
def hunters():
    """Player runs into hunters"""
def hunters_choice():
    """Decide to run back to choice or approach hunters"""
def approach():
    """Approach module, player has to decide to lie, confess, or bribe the hunters"""
def lie():
    """If player decides to lie, the game calls random_lie to decide fate"""
def random_lie():
    """Module randomly chooses between either death_in_woods() or shoreline storyline"""
def death_in_woods():
    """Player dies in woods"""
def confess():
    """Scene where player confesses that they are escaped con. Will call random_confess() to decide
    players fate"""
def random_confess():
    """Player confesses and game will choose between death_in_woods, bridge or road."""
def bribe():
    """Player decides to bribe hunters and players fate is chosen by random draw of either
    death_in_woods or player is allowed to go to the_road()"""
def random_fate():
    """This module is shared by the_bridge() and the_road(). It randomly chooses between 4 different scenarios:
    roadblock(), vehicle(), chopper(), or all_clear()."""
def roadblock():
    """Player runs into a road block. It's the end of the line. Player will either be shot() or captured()."""
def shot():
    """Player is shot"""
def captured():
    """Player is captured"""
def vehicle():
    """Player encounters a vehicle and random_vehicle() module is called to determine fate."""
def random_vehicle():
    """This module will decide if the vehicle is driven by friend() or foe()"""
def foe():
    """If vehicle is driven by foe call roadblock() and pass message"""
def friend():
    """Friendly character encountered. Player is driven to shoreline()."""
def chopper():
    """A chopper starts flying overhead. Call chopper_chance()"""
def chopper_chance():
    """In this module player has to guess a number and if within 1 digit of the number,
    player gets to go back to woods(); or else player gets chased into roadblock()"""
def all_clear():
    """All is clear for player.  module calls shoreline()"""
def canoe():
    """Part of the shoreline() storyline. Player chooses canoe. And, then has a choice of going south() or north()"""
def raft():
    """Part of the shoreline() storyline. Player chooses raft. And, then has to complete:
    raft_challenge_1(), raft_challenge_2() and raft_challenge_3()"""
def go_south():
    """Player decides to go south"""
def go_north():
    """Player decides to go north"""
def rapids():
    """Player sees rapids ahead and must decide quickly whether to run_rapids() or portage_rapids()"""
def portage_rapids():
    """Player decides to portage. If a random number between 1 and 5, player meets hunters(), else reach other_side()."""
def run_rapids():
    """Player decides to run the rapids. If a random number between 1 and 3, player collapse() and dies, 
    else reach other_side()."""
def other_side():
    """Player reaches the other side of river to a town and see's a payphone()."""
def payphone():
    """Player get's in payphone and must complete last_boss() to win."""
def last_boss():
    """Player has 3 chances to complete challenge to win() or be recaptured()."""
def win(player):
    """Winning module"""
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
    time.sleep(3)
    border_msg(f'Congratulations {player}\nYou Have Escaped Dutton Island\n You Are The Best!')
    time.sleep(5)
    credits()

def recaptured():
    """Player is recaptured. A random choice is made whether: death penalty, life, or 15 yrs with paraole in 5."""
    print("This is recaptured")
def death_penalty():
    """Death penalty ending storyline"""
    time.sleep(0.5)
    print("")
    print("There will be no mercy.")
    print("You have been sentenced to death by firing squad.")
    time.sleep(1)
    print("May Darwin have mercy on your soul.")
    time.sleep(3)
    credits()

def life(player):
    """Life imprisonment ending storyline."""
    time.sleep(0.5)
    print("")
    print("The Judge is deliberating.....")
    time.sleep(1.2)
    print(f"{player}, you have been sentenced to life in prison without possibility of parole.")
    time.sleep(3)
    credits()

def parole():
    """15 years with parole after 5 years storyline."""
    time.sleep(0.5)
    print("")
    print("The judge is deliberating......")
    time.sleep(1.5)
    print("The court will be lenient in these matters.")
    time.sleep(0.5)
    print("I sentence you to 15 years in prison. However, if you are a model prisoner, you'll be out in 5 years")
    time.sleep(3)
    credits()

def raft_challenge_1():
    """First of 3 challenges for choosing to raft. If fail call collapse()"""
def raft_challenge_2():
    """Second of 3 challenges for choosing to raft. If fail call collapse()"""
def raft_challenge_3():
    """Last raft challenge. Completing gets player to other_side(). Failure, too close to shore, recaptured()."""
def credits():
    print("")
    print("Escape from Dutton Island")
    print("Concept and coding by Gregory Brown")
    print("Created to demonstrate beginner level competency in Python")
    print("January 2020")
    


welcome(player, lawyers_name)

