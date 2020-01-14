def welcome():
    """Game welcome screen"""
def escape_choice():
    """Give 4 options for player to choose escape path"""
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
def win():
    """Winning module"""
def recaptured():
    """Player is recaptured. A random choice is made whether: death penalty, life, or 15 yrs with paraole in 5."""
def death_penalty():
    """Death penalty ending storyline"""
def life():
    """Life imprisonment ending storyline."""
def parole():
    """15 years with parole after 5 years storyline."""
def raft_challenge_1():
    """First of 3 challenges for choosing to raft. If fail call collapse()"""
def raft_challenge_2():
    """Second of 3 challenges for choosing to raft. If fail call collapse()"""
def raft_challenge_3():
    """Last raft challenge. Completing gets player to other_side(). Failure, too close to shore, recaptured()."""




