#Credits: Mitch Bateup, Sophie Press, Thomas Dubojski, Caleb Francey, Python Community, Pawan Sainni.

#Setting Up Main Game Colours:
class colour:
    purple='\033[95m'
    cyan='\033[96m'
    dark_cyan='\033[36m'
    blue='\033[94m'
    green='\033[92m'
    yellow='\033[93m'
    red='\033[91m'
    bold='\033[1m'
    under_line='\033[4m'
    end='\033[0m'
    
#Setting Up Main Game Functions:
import sys
import os
import random
def scramble(game_word):
    scrambled_word=list(game_word)
    random.shuffle(scrambled_word)
    return ''.join(scrambled_word)

#Setting Up Main Variables:
score=100
attempts_easy_difficulty=6
attempts_medium_difficulty=5
attempts_hard_difficulty=4
game_words_guessed=0

#Setting Up Game Word Lists:
word_list_easy_difficulty=['shine','crazy','have','cigar','wish','were','here','pink','floyd','dire','sick','alice','minus']
word_list_medium_difficulty=[]
word_list_hard_difficulty=[]

#Main Menu:
print('<-----Play----->')
print('<-----Exit----->')
print('<-----Credits----->')
print()
print('<-----Enter the Name of the Option You want to Select:----->')
print()
game_selection=input()
if game_selection=='exit' or game_selection=='Exit' or game_selection=='EXIT' or game_selection=='2':
    os.system('cls')
    print()
    print('Goodbye!')
    print()
    print('<-----Press Enter to Exit----->')
    print()
    input()
    sys.exit()
elif game_selection=='credits' or game_selection=='Credits' or game_selection=='CREDITS' or game_selection=='3':
    os.system('cls')
    print()
    print('<-----Credits----->')
    print()
    print('1) Mitch Bateup - Game Creator, Programmer, Designer, Engineer and Game Tester.')
    print('2) Sophie Press - Idea Creator, Suggestions and Feedback Provider.')
    print('3) Thomas Dubojski - Resource Assistant, Feedback Provider.')
    print('4) Caleb Francey - Resource Assistant, Feedback Provider.')
    print('5) Pawan Sainni - Teacher, Code Provider.')
    print('6) Python Community - Python Programming Language.')
    print()
    print('<-----Special Thanks to the Above People and the Python Community for Their Contributions to this Game!----->')
    print()
    print('Goodbye!')
    print()
    print('<-----Press Enter to Exit----->')
    print()
    input()
    sys.exit()

#Game Introduction:
elif game_selection=='play' or game_selection=='Play' or game_selection=='PLAY' or game_selection=='1':
    os.system('cls')
    print()
    print("<----- Welcome to Mitch's Word Scramble Game! ----->")
    print()
    print('<-----Please Enter Your Name:----->')
    print()
    game_player_name=input()
    os.system('cls')
    print('Hello {}, Nice of You to Play this Game!'.format(game_player_name))

#Difficulty Selection:
    print()
    print('<-----Choose a Difficulty:----->')
    print()
    print('1) Easy Difficulty - 4/5 Letter Words, You get 6 Attempts, You get 2 Hints on the First 2 Letters for Each Question.')
    print('2) Medium Difficulty - 6/7 Letter Words, You get 5 Attempts, You get 1 Hint on the First Letter for Each Question.')
    print('3) Hard Difficulty - 8+ Letter Words, You get 4 Attempts, You get 0 Hints.')
    print()
    print('<-----Enter the Name of the Difficulty You want to Play:----->')
    print()
    difficulty_selection=input()

#Easy Difficulty:
    if difficulty_selection=='easy' or difficulty_selection=='Easy' or difficulty_selection=='EASY' or difficulty_selection=='e' or difficulty_selection=='E' or difficulty_selection=='1':
        os.system('cls')
        game_difficulty_name='Easy'
        print()
        print('You have Chosen Easy Difficulty!')
        print()
        print('<-----Easy Difficulty Breif:----->')
        print()
        print('- You will Unscramble 4/5 Letter Words.')
        print('- You Start with 100 Points.')
        print('- You get 6 Attempts.')
        print('- You have an Option to choose 2 Hints on Each Question.')
        print('- If You try to get more than 2 Hints, You will Lose 10 Points.')
        print('- Each Correct Guess Earns 20 Points.')
        print('- Each Incorrect Guess Loses 10 Points.')
        print('- Each Incorrect Guess Loses 1 Attempt.')
        print('- You can Skip Questions but You Lose 10 Points.')
        print()
        print('Get as Far as You can!')
        print("Good Luck, Let's Go!")
        while attempts_easy_difficulty>0:
            os.system('cls')
            game_word=random.choice(word_list_easy_difficulty)
            shuffled_word=scramble(game_word)
            scrambled_word=list(game_word)
            easy_difficulty_hint_1=scrambled_word[0]
            easy_difficulty_hint_2=scrambled_word[1]
            print()
            print('<-----Question:----->')
            print()
            print('<-----Score: {}----->'.format(score))
            print('<-----Attempts Left: {}----->'.format(attempts_easy_difficulty))
            print("<-----Skip: (Type 'Skip')----->")
            print("<-----Hint: (Type 'Hint')----->")
            print()
            print('Scrambled Word:')
            print(shuffled_word)
            print()
            guess_word=input()
            if guess_word==game_word:
                os.system('cls')
                print()
                print('Correct! +20 Points.')
                score=score+20
                game_words_guessed=game_words_guessed+1
            elif guess_word=='skip' or guess_word=='Skip' or guess_word=='SKIP':
                os.system('cls')
                print()
                print('Question Skipped! -10 Points.')
                score=score-10
            elif guess_word=='hint' or guess_word=='Hint' or guess_word=='HINT':
                os.system('cls')
                print()
                print('<-----This is Your First Hint----->')
                print()
                print('<-----Score: {}----->'.format(score))
                print('<-----Attempts Left: {}----->'.format(attempts_easy_difficulty))
                print("<-----Skip: (Type 'Skip')----->")
                print("<-----Hint: (Type 'Hint')----->")
                print()
                print('Scrambled Word:')
                print(shuffled_word)
                print('Hint 1: First Letter is {}.'.format(easy_difficulty_hint_1))
                print()
                guess_word=input()
                if guess_word==game_word:
                    os.system('cls')
                    print()
                    print('Correct! +20 Points.')
                    score=score+20
                    game_words_guessed=game_words_guessed+1
                elif guess_word=='skip' or guess_word=='Skip' or guess_word=='SKIP':
                    os.system('cls')
                    print()
                    print('Question Skipped! -10 Points.')
                    score=score-10
                elif guess_word=='hint' or guess_word=='Hint' or guess_word=='HINT':
                    os.system('cls')
                    print()
                    print('<-----This is Your Second and Last Hint----->')
                    print()
                    print('<-----Score: {}----->'.format(score))
                    print('<-----Attempts Left: {}----->'.format(attempts_easy_difficulty))
                    print("<-----Skip: (Type 'Skip')----->")
                    print()
                    print('Scrambled Word:')
                    print(shuffled_word)
                    print('Hint 1: First Letter is {}.'.format(easy_difficulty_hint_1))
                    print('Hint 2: Second Letter is {}.'.format(easy_difficulty_hint_2))
                    print()
                    guess_word=input()
                    if guess_word==game_word:
                        os.system('cls')
                        print()
                        print('Correct! +20 Points.')
                        score=score+20
                        game_words_guessed=game_words_guessed+1
                    elif guess_word=='skip' or guess_word=='Skip' or guess_word=='SKIP':
                        os.system('cls')
                        print()
                        print('Question Skipped! -10 Points.')
                        score=score-10
                    elif guess_word=='hint' or guess_word=='Hint' or guess_word=='HINT':
                        os.system('cls')
                        print()
                        print('Your Out of Hints! -10 Points.')
                        score=score-10
                    else:
                        os.system('cls')
                        print()
                        print('Incorrect! -10 Points, -1 Attempt.')
                        score=score-10
                        attempts_easy_difficulty=attempts_easy_difficulty-1
                else:
                    os.system('cls')
                    print()
                    print('Incorrect! -10 Points, -1 Attempt.')
                    score=score-10
                    attempts_easy_difficulty=attempts_easy_difficulty-1
            else:
                os.system('cls')
                print()
                print('Incorrect! -10 Points, -1 Attempt.')
                score=score-10
                attempts_easy_difficulty=attempts_easy_difficulty-1
        if attempts_easy_difficulty==0:
            os.system('cls')
            final_attempts_number=attempts_easy_difficulty
            print()
            print('<-----Your Out of Attempts!----->')
            print()
            print('Game Over!')

#Medium Difficulty:
    elif difficulty_selection=='medium' or difficulty_selection=='Medium' or difficulty_selection=='MEDIUM' or difficulty_selection=='m' or difficulty_selection=='M' or difficulty_selection=='2':
        os.system('cls')
        game_difficulty_name='Medium'
        print()
        print('You have Chosen Medium Difficulty!')
        print()
        print('<-----Medium Difficulty Breif:----->')
        print()
        print('- You will Unscramble 6/7 Letter Words.')
        print('- You Start with 100 Points.')
        print('- You get 5 Attempts.')
        print('- You have an Option to choose 1 Hint on Each Question.')
        print('- If You try to get more than 1 Hint, You will Lose 10 Points.')
        print('- Each Correct Guess Earns 20 Points.')
        print('- Each Incorrect Guess Loses 10 Points.')
        print('- Each Incorrect Guess Loses 1 Attempt.')
        print('- You can Skip Questions but You Lose 10 Points.')
        print()
        print('Get as Far as You can!')
        print("Good Luck, Let's Go!")
        while attempts_medium_difficulty>0:
            os.system('cls')
            game_word=random.choice(word_list_medium_difficulty)
            shuffled_word=scramble(game_word)
            scrambled_word=list(game_word)
            medium_difficulty_hint=scrambled_word[0]
            print()
            print('<-----Question:----->')
            print()
            print('<-----Score: {}----->'.format(score))
            print('<-----Attempts Left: {}----->'.format(attempts_medium_difficulty))
            print("<-----Skip: (Type 'Skip')----->")
            print("<-----Hint: (Type 'Hint')----->")
            print()
            print('Scrambled Word:')
            print(shuffled_word)
            print()
            guess_word=input()
            if guess_word==game_word:
                os.system('cls')
                print()
                print('Correct! +20 Points.')
                score=score+20
                game_words_guessed=game_words_guessed+1
            elif guess_word=='skip' or guess_word=='Skip' or guess_word=='SKIP':
                os.system('cls')
                print()
                print('Question Skipped! -10 Points.')
                score=score-10
            elif guess_word=='hint' or guess_word=='Hint' or guess_word=='HINT':
                os.system('cls')
                print()
                print('<-----This is Your First and Last Hint----->')
                print()
                print('<-----Score: {}----->'.format(score))
                print('<-----Attempts Left: {}----->'.format(attempts_medium_difficulty))
                print("<-----Skip: (Type 'Skip')----->")
                print()
                print('Scrambled Word:')
                print(shuffled_word)
                print()
                print('Hint: First Letter is {}.'.format(medium_difficulty_hint))
                print()
                guess_word=input()
                if guess_word==game_word:
                    os.system('cls')
                    print()
                    print('Correct! +20 Points.')
                    score=score+20
                    game_words_guessed=game_words_guessed+1
                elif guess_word=='skip' or guess_word=='Skip' or guess_word=='SKIP':
                    os.system('cls')
                    print()
                    print('Question Skipped! -10 Points.')
                    score=score-10
                elif guess_word=='hint' or guess_word=='Hint' or guess_word=='HINT':
                    os.system('cls')
                    print()
                    print('Your Out of Hints! -10 Points.')
                    score=score-10
                else:
                    os.system('cls')
                    print()
                    print('Incorrect! -10 Points, -1 Attempt.')
                    score=score-10
                    attempts_medium_difficulty=attempts_medium_difficulty-1
            else:
                os.system('cls')
                print()
                print('Incorrect! -10 Points, -1 Attempt.')
                score=score-10
                attempts_medium_difficulty=attempts_medium_difficulty-1
        if attempts_medium_difficulty==0:
            os.system('cls')
            final_attempts_number=attempts_medium_difficulty
            print()
            print('<-----Your Out of Attempts!----->')
            print()
            print('Game Over!')
                    
#Hard Difficulty:
    elif difficulty_selection=='hard' or difficulty_selection=='Hard' or difficulty_selection=='HARD' or difficulty_selection=='h' or difficulty_selection=='H' or difficulty_selection=='3':
        os.system('cls')
        game_difficulty_name='Hard'
        print()
        print('You have Chosen Hard Difficulty!')
        print()
        print('<-----Hard Difficulty Breif:----->')
        print()
        print('- You will Unscramble 8+ Letter Words.')
        print('- You Start with 100 Points.')
        print('- You get 4 Attempts.')
        print('- You have 0 Hints.')
        print('- If You try to get Hints, You will Lose 10 Points.')
        print('- Each Correct Guess Earns 20 Points.')
        print('- Each Incorrect Guess Loses 10 Points.')
        print('- Each Incorrect Guess Loses 1 Attempt.')
        print('- You can Skip Questions but You Lose 10 Points.')
        print()
        print('Get as Far as You can!')
        print("Good Luck, Let's Go!")
        while attempts_hard_difficulty>0:
            os.system('cls')
            game_word=random.choice(word_list_hard_difficulty)
            shuffled_word=scramble(game_word)
            print()
            print('<-----Question:----->')
            print()
            print('<-----Score: {}----->'.format(score))
            print('<-----Attempts Left: {}----->'.format(attempts_hard_difficulty))
            print("<-----Skip: (Type 'Skip')----->")
            print()
            print('Scrambled Word:')
            print(shuffled_word)
            print()
            guess_word=input()
            if guess_word==game_word:
                os.system('cls')
                print()
                print('Correct! +20 Points.')
                score=score+20
                game_words_guessed=game_words_guessed+1
            elif guess_word=='skip' or guess_word=='Skip' or guess_word=='SKIP':
                os.system('cls')
                print()
                print('Question Skipped! -10 Points.')
                score=score-10
            else:
                os.system('cls')
                print()
                print('Incorrect! -10 Points, -1 Attempt.')
                score=score-10
                attempts_hard_difficulty=attempts_hard_difficulty-1
        if attempts_hard_difficulty==0:
            os.system('cls')
            final_attempts_number=attempts_hard_difficulty
            print()
            print('<-----Your Out of Attempts!----->')
            print()
            print('Game Over!')
        
#Invalid Difficulty Selection on Difficulty Selection:
    else:
        os.system('cls')
        print()
        print('<-----Invalid Difficulty Selection!----->')
        print("Try Entering a Valid Difficulty Selection: (Type 'Easy' or 'Medium' or 'Hard')")
        print()
        print('Goodbye!')
        print()
        print('<-----Press Enter to Exit----->')
        print()
        input()
        sys.exit()
        
#Invalid Game Selection on Main Menu:
else:
    os.system('cls')
    print()
    print('<-----Invalid Game Selection!----->')
    print("Try Entering a Valid Game Selection: (Type 'Play' or 'Exit' or 'Credits')")
    print()
    print('Goodbye!')
    print()
    print('<-----Press Enter to Exit----->')
    print()
    input()
    sys.exit()
    
#End Of Game Summary:
os.system('cls')  
print()
print('<-----Game Summary----->')
print()
print('Player Name: {}'.format(game_player_name))
print('Difficulty Played: {}'.format(game_difficulty_name))
print('Final Score: {}'.format(score))
print('Words Guessed: {}'.format(game_words_guessed))
print('Attempts Left: {}'.format(final_attempts_number))
if score<=60 and game_words_guessed==0:
    print()
    print("Maybe this Game isn't for You...")
elif score>60 and game_words_guessed==0:
    print()
    print('Bad Luck! Try to get Further!')
elif score>1000 and game_words_guessed>50:
    print()
    print('Wow! Amazing Work.')
else:
    print()
    print('Well Done!')

#Game Conclusion:
print()
print("<-----Thank You for Playing Mitch's Word Scramble Game!----->")
print()
print('Goodbye!')
print()
print('<-----Press Enter to Exit----->')
print()
input()
sys.exit()
