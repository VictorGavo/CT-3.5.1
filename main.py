"""
    For this project, you will individually create a program that has a "player" and a "computer" advisary. The computer
     should randomly choose it's decision based on a list of actions it can take ("Rock", "Paper" or "Scissors"). The player
     should then have a chance to input their decision. If player and computer choose the same decision then display 
     ("Game Tied"), If the player chooses "Rock" and the computer chooses "Paper" display ("You lose"), if the player 
     chooses "Scissors" and the computer chooses "Rock" display ("You Lose") and if the player chooses "Paper" and the 
     computer chooses "Scissors" then display ("You lose") -- Vice versa for other descisions.

    Continue to ask the player for their input until they say "I quit", at which time the game will then end and display
     ("Thank you for playing").

    In this project, you will need to use the random.randint function to enable to computer to make a random decision. 
    Full documentation on the use of this function is attached in a link to this assignment.

    Once completed, commit your code to github and submit the link to this assignment.
"""

from random import randint

class rPS():
    def __init__(self):
        self.options = ['Rock', 'Paper', 'Scissors']
        self.pc_choice = ''
        self.npc_choice = ''
        self.score = {}
        self.pc = ''

    def menu(self):
        """
            This is the menu where the player will be able to choose to play a game and the current score will be displayed
        """

        print("Come one, come all and face the fearsome Rock, Paper, Scissor-inator 3000!")
        print("Test your mettle against this powerhouse of a program!")
        self.pc = input("You there! Living creature, what is your name? ")
        answer = input(f"Well, brave {self.pc.title()}, do you dare face this fearsome foe?? (y/n) ")
        if answer.lower() == 'y':
            self.score = {'Bender Bending Rodriguez': 0, self.pc.title(): 0}
            self.play()
        elif answer.lower() == 'n':
            print("it would seem the only way to win is not to play...")
        else:
            print(f"My dear {self.pc.title()}, please enter a simple 'y' for yes, or a 'n' for no.")

    def play(self):
        """
            Handles the act of choosing/assigning what the pc and npc will play. (rock/paper/scissors)
        """
        print("""
                Which do you choose?
                r | Rock
                p | Paper
                s | Scissors
                q | Quit
                """)
        while True:
            choice = input(">")
            if choice.lower() == 'r':
                self.pc_choice = self.options[0]
                self.npc_choice = self.options[randint(0,2)]
                print(f"Bender is deciding...{self.npc_choice}")
                self.rules()
            elif choice.lower() == 'p':
                self.pc_choice = self.options[1]
                self.npc_choice = self.options[randint(0,2)]
                print(f"Bender is deciding...{self.npc_choice}")
                self.rules()
            elif choice.lower() == 's':
                self.pc_choice = self.options[2]
                self.npc_choice = self.options[randint(0,2)]
                print(f"Bender is deciding...{self.npc_choice}")
                self.rules()
            elif choice.lower() == 'q':
                False
                break
            else:
                print("Ah, ah, ah. That is not a valid choice, my friend.")
        self.endgame()
        

    def rules(self):
        """
            Handles deciding who wins, PC or NPC
        """
    # PC Win Conditions
        if self.pc_choice == 'Rock' and self.npc_choice == 'Scissors':
            self.score[self.pc] += 1
            print("Amazing! You won!")
            print(f"{self.pc} | {self.score[self.pc]} || {self.score['Bender Bending Rodriguez']} | Bender Bending Rodriguez")
        elif self.pc_choice == 'Paper' and self.npc_choice == 'Rock':
            self.score[self.pc] += 1
            print("Amazing! You won!")
            print(f"{self.pc} | {self.score[self.pc]} || {self.score['Bender Bending Rodriguez']} | Bender Bending Rodriguez")
        elif self.pc_choice == 'Scissors' and self.npc_choice == 'Paper':
            self.score[self.pc] += 1
            print("Amazing! You won!")
            print(f"{self.pc} | {self.score[self.pc]} || {self.score['Bender Bending Rodriguez']} | Bender Bending Rodriguez")
    # NPC Win Conditions
        elif self.pc_choice == 'Rock' and self.npc_choice == 'Paper':
            self.score['Bender Bending Rodriguez'] += 1
            print("To be expected, machine wins!")
            print(f"{self.pc} | {self.score[self.pc]} || {self.score['Bender Bending Rodriguez']} | Bender Bending Rodriguez")
        elif self.pc_choice == 'Paper' and self.npc_choice == 'Scissors':
            self.score['Bender Bending Rodriguez'] += 1
            print("To be expected, machine wins!")
            print(f"{self.pc} | {self.score[self.pc]} || {self.score['Bender Bending Rodriguez']} | Bender Bending Rodriguez")
        elif self.pc_choice == 'Scissors' and self.npc_choice == 'Rock':
            self.score['Bender Bending Rodriguez'] += 1
            print("To be expected, machine wins!")
            print(f"{self.pc} | {self.score[self.pc]} || {self.score['Bender Bending Rodriguez']} | Bender Bending Rodriguez")
        else:
            print("Wow! A tie!")
        self.play()

    def endgame(self):
        print("Game over man!")
        print("Final Score:")
        print(f"{self.pc} | {self.score[self.pc]} || {self.score['Bender Bending Rodriguez']} | Bender Bending Rodriguez")
        if self.score[self.pc] > self.score['Bender Bending Rodriguez']:
            print("Why I don't believe it! Well... I guess everyone gets lucky now and again.")
        elif self.score[self.pc] < self.score['Bender Bending Rodriguez']:
            print("As expected, well... Better luck next time!")
        else:
            print("A tie! Smart to quit as close as you will get to winning! ;)")
        print("Thanks for playing!")
        quit()

test = rPS()
test.menu()