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
word_list_easy_mode=['shine','crazy','have','cigar','wish','were','here','pink','floyd','dire','sick','alice','minus']
word_list_medium_mode=[]
word_list_hard_mode=[]

#Introduction:
print("<----- Welcome to Mitch's Word Scramble Game! ----->")
print()
print('<-----Please Enter Your Name:----->')
print()
player_name=input()
print('Hello {}, Nice of You to Play this Game!'.format(player_name))

#Mode Selection:
print()
print('<-----Choose a Difficulty:----->')
print()
print('1) Easy Mode - 4/5 Letter Words, You get 6 Attempts, You get 2 Hints on the First 2 Letters for Each Question.')
print('2) Medium Mode - 6/7 Letter Words, You get 5 Attempts, You get 1 Hint on the First Letter for Each Question.')
print('3) Hard Mode - 8+ Letter Words, You get 4 Attempts, You get 0 Hints.')
print()
print('<-----Enter the Name of the Mode You want to Play:----->')
mode_selection=input()

#Easy Mode:
if mode_selection=='easy' or mode_selection=='Easy' or mode_selection=='EASY' or mode_selection=='e' or mode_selection=='E' or mode_selection=='1':
    print()
    print('You have Chosen Easy Mode!')
    print()
    print('<-----Easy Mode Breif:----->')
    print()
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
    while attempts_easy_mode>0:
        game_word=random.choice(word_list_easy_mode)
        shuffled_word=scramble(game_word)
        scrambled_word=list(game_word)
        easy_mode_hint_1=scrambled_word[0]
        easy_mode_hint_2=scrambled_word[1]
        print()
        print('<-----Question:----->')
        print()
        print('<-----Score: {}----->'.format(score))
        print('<-----Attempts Left: {}----->'.format(attempts_easy_mode))
        print("<-----Skip: (Type 'Skip')----->")
        print("<-----Hint: (Type 'Hint')----->")
        print()
        print('Scrambled Word:')
        print(shuffled_word)
        print()
        guess_word=input()
        if guess_word==game_word:
            print()
            print('Correct! +20 Points.')
            score=score+20
            words_guessed=words_guessed+1
        elif guess_word=='skip' or guess_word=='Skip' or guess_word=='SKIP':
            print()
            print('Question Skipped! -10 Points.')
            score=score-10
        elif guess_word=='hint' or guess_word=='Hint' or guess_word=='HINT':
            print()
            print('<-----This is Your First Hint----->')
            print()
            print('<-----Score: {}----->'.format(score))
            print('<-----Attempts Left: {}----->'.format(attempts_easy_mode))
            print("<-----Skip: (Type 'Skip')----->")
            print("<-----Hint: (Type 'Hint')----->")
            print()
            print('Scrambled Word:')
            print(shuffled_word)
            print('Hint 1: First Letter is {}.'.format(easy_mode_hint_1))
            print()
            guess_word=input()
            if guess_word==game_word:
                print()
                print('Correct! +20 Points.')
                score=score+20
                words_guessed=words_guessed+1
            elif guess_word=='skip' or guess_word=='Skip' or guess_word=='SKIP':
                print()
                print('Question Skipped! -10 Points.')
                score=score-10
            elif guess_word=='hint' or guess_word=='Hint' or guess_word=='HINT':
                print()
                print('<-----This is Your Second and Last Hint----->')
                print()
                print('<-----Score: {}----->'.format(score))
                print('<-----Attempts Left: {}----->'.format(attempts_easy_mode))
                print("<-----Skip: (Type 'Skip')----->")
                print()
                print('Scrambled Word:')
                print(shuffled_word)
                print('Hint 1: First Letter is {}.'.format(easy_mode_hint_1))
                print('Hint 2: Second Letter is {}.'.format(easy_mode_hint_2))
                print()
                guess_word=input()
                if guess_word==game_word:
                    print()
                    print('Correct! +20 Points.')
                    score=score+20
                    words_guessed=words_guessed+1
                elif guess_word=='skip' or guess_word=='Skip' or guess_word=='SKIP':
                    print()
                    print('Question Skipped! -10 Points.')
                    score=score-10
                elif guess_word=='hint' or guess_word=='Hint' or guess_word=='HINT':
                    print()
                    print('Your Out of Hints! -10 Points.')
                    score=score-10
                else:
                    print()
                    print('Incorrect! -10 Points, -1 Attempt.')
                    score=score-10
                    attempts_easy_mode=attempts_easy_mode-1
            else:
                print()
                print('Incorrect! -10 Points, -1 Attempt.')
                score=score-10
                attempts_easy_mode=attempts_easy_mode-1
        else:
            print()
            print('Incorrect! -10 Points, -1 Attempt.')
            score=score-10
            attempts_easy_mode=attempts_easy_mode-1
    if attempts_easy_mode==0:
        final_attempts_number=attempts_easy_mode
        print()
        print('<-----Your out of Attempts!----->')
        print()
        print('Game Over!')
                    
        
        
        
#Medium Mode:


#Hard Mode:


#End Of Game Summary:


#Conclusion:
