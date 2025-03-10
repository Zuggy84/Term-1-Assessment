#Credits: Mitch Bateup, Sophie Press.

#Setting Up Main Game Functions:
import random
def scramble(game_word):
    scrambled_word=list(game_word)
    random.shuffle(scrambled_word)
    return ''.join(scrambled_word)

#Setting Up Main Variables:
score=100
attempts_easy_mode=6
attempts_medium_mode=5
attempts_hard_mode=4
words_guessed=0

#Setting Up Game Word Lists:
word_list_easy_mode=[]
word_list_medium_mode=[]
word_list_hard_mode=[]

#Introduction:
print("<----- Welcome to Mitch's Word Scramble Game! ----->")
print()
print('<-----Please Enter Your Name:----->')
player_name=input()
print('Hello {}, Nice of You to Play this Game!'.format(player_name))

#Mode Selection:
print()
print('<-----Choose a Difficulty:----->')
print()
print('1) Easy Mode - You get 6 Attempts, Words have 2 Capitals when Scrambled.')
print('2) Medium Mode - You get 5 Attempts, Words have 1 Capital when Scrambled.')
print('3) Hard Mode - You get 4 Attempts, Scrambled Words have 0 Capitals.')
print()
print('<-----Enter the Name of the Mode You want to Play:----->')
mode_selection=input()

#Easy Mode:
if mode_selection=='easy' or mode_selection=='Easy' or mode_selection=='EASY' or mode_selection=='e' or mode_selection=='E' or mode_selection=='1':
    print()
    print('You have Chosen Easy Mode!')
    print('<-----Easy Mode Breif:----->')
    print()
    print('-You Start with 100 Points.')
    print('-You get 6 Attempts.')
    print('-Words have 2 Capitals.')
    print('-Each Correct Guess Earns 20 Points.')
    print('-Each Incorrect Guess Loses 10 Points.')
    print('-Each Incorrect Guess Loses 1 Attempt.')
    print('-You can Skip Questions but You Lose 10 Points.')
    print()
    print('Get as Far as You can!')
    print("Good Luck, Let's Go!")

#Medium Mode:


#Hard Mode:


#End Of Game Summary:


#Conclusion:
