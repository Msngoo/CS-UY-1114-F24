class Student:
    def __init__(self, name, selection="", choices=["Rock", "Paper", "Scissors"], wins=0):
        self.selection = selection
        self.choices = choices
        self.name = name
        self.wins = wins
    '''
        Alternatively Easier Method for Default Instance Variables/ Attributes:

    def __init__(self, name):
        self.name = name
        self.selection = ""
        self.choices = ["Rock", "Paper", "Scissors"]
        self.wins = 0
    '''
    def __str__(self):
        return f"{self.name} has won {self.wins} round(s) of rock paper scissors!"
    
    def pick_hand(self):
        import random
        self.selection = random.choice(self.choices)
    
    def win_match(self):
         self.wins += 1

def play_game(p1, p2):
        p1_hand = p1.pick_hand()
        p2_hand = p2.pick_hand()
        if p1_hand == "Rock" and p2_hand == "Scissors" or  \
            p1_hand == "Scissors" and p2_hand == "Paper" or \
            p1_hand == "Paper" and p2_hand == "Rock":
            return p1.win_match()        

def main():
    bob = Student("Bob")
    carl = Student("Carl")
    while bob.wins != 2 and carl.wins != 2:
        play_game(bob, carl)
    print(bob)
    print(carl)

main()