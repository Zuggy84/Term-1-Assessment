#Credits: Mitch Bateup, Sophie Press, Thomas Dubojski, Caleb Francey, Python Community, Pawan Sainni.

#Setting Up Main Game Colours:
class colour:
    purple='\033[95m'
    cyan='\033[96m'
    blue='\033[94m'
    green='\033[92m'
    yellow='\033[93m'
    red='\033[91m'
    orange='\033[33m'
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
os.system('cls')
print(colour.cyan+'<-----'+colour.green+colour.under_line+'1) Play'+colour.end+colour.cyan+'----->'+colour.end)
print(colour.cyan+'<-----'+colour.red+colour.under_line+'2) Exit'+colour.end+colour.cyan+'----->'+colour.end)
print(colour.cyan+'<-----'+colour.yellow+colour.under_line+'3) Credits'+colour.end+colour.cyan+'----->'+colour.end)
print()
print(colour.cyan+'<-----Enter the Name of the Option You want to Select:----->'+colour.end)
print()
game_selection=input()
if game_selection=='exit' or game_selection=='Exit' or game_selection=='EXIT' or game_selection=='2':
    os.system('cls')
    print()
    print(colour.cyan+colour.under_line+'<-----'+colour.red+'Exit'+colour.cyan+'----->'+colour.end)
    print()
    print(colour.cyan+'Goodbye!'+colour.end)
    print()
    print(colour.cyan+'<-----'+colour.red+'Press Enter to Exit'+colour.cyan+'----->'+colour.end)
    print()
    input()
    sys.exit()
elif game_selection=='credits' or game_selection=='Credits' or game_selection=='CREDITS' or game_selection=='3':
    os.system('cls')
    print()
    print(colour.cyan+colour.under_line+'<-----'+colour.yellow+'Credits'+colour.cyan+'----->'+colour.end)
    print()
    print(colour.yellow+'1) Mitch Bateup - Game Creator, Programmer, Designer, Engineer and Game Tester.'+colour.end)
    print(colour.yellow+'2) Sophie Press - Idea Creator, Suggestions and Feedback Provider.'+colour.end)
    print(colour.yellow+'3) Thomas Dubojski - Resource Assistant, Feedback Provider.'+colour.end)
    print(colour.yellow+'4) Caleb Francey - Resource Assistant, Feedback Provider.'+colour.end)
    print(colour.yellow+'5) Pawan Saini - Teacher, Code Provider.'+colour.end)
    print(colour.yellow+'6) Python Community - Python Programming Language.'+colour.end)
    print()
    print(colour.blue+'<-----Special Thanks to the Above People and the Python Community for Their Contributions to this Game!----->'+colour.end)
    print()
    print(colour.cyan+'Goodbye!'+colour.end)
    print()
    print(colour.cyan+'<-----'+colour.red+'Press Enter to Exit'+colour.cyan+'----->'+colour.end)
    print()
    input()
    sys.exit()

#Game Introduction:
elif game_selection=='play' or game_selection=='Play' or game_selection=='PLAY' or game_selection=='1':
    os.system('cls')
    print()
    print(colour.cyan+colour.under_line+'<-----'+colour.green+'Play'+colour.cyan+'----->'+colour.end)
    print()
    print(colour.blue+"<----- Welcome to Mitch's Word Scramble Game! ----->"+colour.end)
    print()
    print(colour.cyan+'<-----Please Enter Your Name:----->'+colour.end)
    print()
    game_player_name=input()
    file=open('D:/School/Python/Year 11 - Term 1 Assessment - 2025/Save Files/Player List/Player Name.txt','a')
    file=file.write('{}, '.format(game_player_name))
    os.system('cls')
    print(colour.cyan+'Hello '+colour.purple+colour.bold+'{}'.format(game_player_name)+colour.end+colour.cyan+', Nice of You to Play this Game!'+colour.end)
    print()
    print(colour.cyan+'<-----Press Enter to Continue----->'+colour.end)
    print()
    input()

#Difficulty Selection:
    os.system('cls')
    print()
    print(colour.cyan+'<-----Choose a Difficulty:----->'+colour.end)
    print()
    print(colour.green+colour.under_line+'1) Easy Difficulty'+colour.end+colour.green+' - 4/5 Letter Words, You get 6 Attempts, You get 2 Hints on the First 2 Letters for Each Question.'+colour.end)
    print(colour.yellow+colour.under_line+'2) Medium Difficulty'+colour.end+colour.yellow+' - 6/7 Letter Words, You get 5 Attempts, You get 1 Hint on the First Letter for Each Question.'+colour.end)
    print(colour.red+colour.under_line+'3) Hard Difficulty'+colour.end+colour.red+' - 8+ Letter Words, You get 4 Attempts, You get 0 Hints.'+colour.end)
    print()
    print(colour.cyan+'<-----Enter the Name of the Difficulty You want to Play:----->'+colour.end)
    print()
    difficulty_selection=input()

#Easy Difficulty:
    if difficulty_selection=='easy' or difficulty_selection=='Easy' or difficulty_selection=='EASY' or difficulty_selection=='e' or difficulty_selection=='E' or difficulty_selection=='1':
        os.system('cls')
        game_difficulty_name='Easy'
        print()
        print(colour.cyan+'You have Chosen '+colour.green+'Easy'+colour.cyan+' Difficulty!'+colour.end)
        print()
        print(colour.cyan+colour.under_line+'<-----'+colour.green+'Easy Difficulty Breif:'+colour.cyan+'----->'+colour.end)
        print()
        print(colour.green+'- You will Unscramble 4/5 Letter Words.'+colour.end)
        print(colour.green+'- You Start with 100 Points.'+colour.end)
        print(colour.green+'- You get 6 Attempts.'+colour.end)
        print(colour.green+'- You have an Option to choose 2 Hints on Each Question.'+colour.end)
        print(colour.green+'- If You try to get more than 2 Hints, You will Lose 10 Points.'+colour.end)
        print(colour.green+'- Each Correct Guess Earns 20 Points.'+colour.end)
        print(colour.green+'- Each Incorrect Guess Loses 10 Points.'+colour.end)
        print(colour.green+'- Each Incorrect Guess Loses 1 Attempt.'+colour.end)
        print(colour.green+'- You can Skip Questions but You Lose 10 Points.'+colour.end)
        print()
        print(colour.blue+'Get as Far as You can!'+colour.end)
        print(colour.blue+"Good Luck, Let's Go!"+colour.end)
        print()
        print(colour.cyan+'<-----Press Enter to Continue----->'+colour.end)
        print()
        input()
        os.system('cls')
        while attempts_easy_difficulty>0:
            os.system('cls')
            game_word=random.choice(word_list_easy_difficulty)
            shuffled_word=scramble(game_word)
            scrambled_word=list(game_word)
            easy_difficulty_hint_1=scrambled_word[0]
            easy_difficulty_hint_2=scrambled_word[1]
            print()
            print(colour.cyan+colour.under_line+'<-----Question:----->'+colour.end)
            print()
            print(colour.cyan+'<-----Score: '+colour.blue+'{}'.format(score)+colour.cyan+'----->'+colour.end)
            print(colour.cyan+'<-----Attempts Left: '+colour.blue+'{}'.format(attempts_easy_difficulty)+colour.cyan+'----->'+colour.end)
            print(colour.cyan+"<-----Skip: "+colour.blue+"(Type 'Skip')"+colour.cyan+"----->"+colour.end)
            print(colour.cyan+"<-----Hint: "+colour.blue+"(Type 'Hint')"+colour.cyan+"----->"+colour.end)
            print()
            print(colour.cyan+'Scrambled Word:'+colour.end)
            print(colour.orange+shuffled_word+colour.end)
            print()
            guess_word=input()
            if guess_word==game_word:
                os.system('cls')
                print()
                print(colour.green+'Correct! +20 Points.'+colour.end)
                score=score+20
                game_words_guessed=game_words_guessed+1
                print()
                print(colour.cyan+'<-----Press Enter to Continue----->'+colour.end)
                print()
                input()
            elif guess_word=='skip' or guess_word=='Skip' or guess_word=='SKIP':
                os.system('cls')
                print()
                print(colour.yellow+'Question Skipped! -10 Points.'+colour.end)
                score=score-10
                print()
                print(colour.cyan+'<-----Press Enter to Continue----->'+colour.end)
                print()
                input()
            elif guess_word=='hint' or guess_word=='Hint' or guess_word=='HINT':
                os.system('cls')
                print()
                print(colour.cyan+colour.under_line+'<-----This is Your First Hint----->'+colour.end)
                print()
                print(colour.cyan+'<-----Score: '+colour.blue+'{}'.format(score)+colour.cyan+'----->'+colour.end)
                print(colour.cyan+'<-----Attempts Left: '+colour.blue+'{}'.format(attempts_easy_difficulty)+colour.cyan+'----->'+colour.end)
                print(colour.cyan+"<-----Skip: "+colour.blue+"(Type 'Skip')"+colour.cyan+"----->"+colour.end)
                print(colour.cyan+"<-----Hint: "+colour.blue+"(Type 'Hint')"+colour.cyan+"----->"+colour.end)
                print()
                print(colour.cyan+'Scrambled Word:'+colour.end)
                print(colour.orange+shuffled_word+colour.end)
                print(colour.cyan+'Hint 1: First Letter is '+colour.orange+'{}'.format(easy_difficulty_hint_1)+colour.cyan+'.'+colour.end)
                print()
                guess_word=input()
                if guess_word==game_word:
                    os.system('cls')
                    print()
                    print(colour.green+'Correct! +20 Points.'+colour.end)
                    score=score+20
                    game_words_guessed=game_words_guessed+1
                    print()
                    print(colour.cyan+'<-----Press Enter to Continue----->'+colour.end)
                    print()
                    input()
                elif guess_word=='skip' or guess_word=='Skip' or guess_word=='SKIP':
                    os.system('cls')
                    print()
                    print(colour.yellow+'Question Skipped! -10 Points.'+colour.end)
                    score=score-10
                    print()
                    print(colour.cyan+'<-----Press Enter to Continue----->'+colour.end)
                    print()
                    input()
                elif guess_word=='hint' or guess_word=='Hint' or guess_word=='HINT':
                    os.system('cls')
                    print()
                    print(colour.cyan+colour.under_line+'<-----This is Your Second and Last Hint----->'+colour.end)
                    print()
                    print(colour.cyan+'<-----Score: '+colour.blue+'{}'.format(score)+colour.cyan+'----->'+colour.end)
                    print(colour.cyan+'<-----Attempts Left: '+colour.blue+'{}'.format(attempts_easy_difficulty)+colour.cyan+'----->'+colour.end)
                    print(colour.cyan+"<-----Skip: "+colour.blue+"(Type 'Skip')"+colour.cyan+"----->"+colour.end)
                    print()
                    print(colour.cyan+'Scrambled Word:'+colour.end)
                    print(colour.orange+shuffled_word+colour.end)
                    print(colour.cyan+'Hint 1: First Letter is '+colour.orange+'{}'.format(easy_difficulty_hint_1)+colour.cyan+'.'+colour.end)
                    print(colour.cyan+'Hint 2: Second Letter is '+colour.orange+'{}'.format(easy_difficulty_hint_2)+colour.cyan+'.'+colour.end)
                    print()
                    guess_word=input()
                    if guess_word==game_word:
                        os.system('cls')
                        print()
                        print(colour.green+'Correct! +20 Points.'+colour.end)
                        score=score+20
                        game_words_guessed=game_words_guessed+1
                        print()
                        print(colour.cyan+'<-----Press Enter to Continue----->'+colour.end)
                        print()
                        input()
                    elif guess_word=='skip' or guess_word=='Skip' or guess_word=='SKIP':
                        os.system('cls')
                        print()
                        print(colour.yellow+'Question Skipped! -10 Points.'+colour.end)
                        score=score-10
                        print()
                        print(colour.cyan+'<-----Press Enter to Continue----->'+colour.end)
                        print()
                        input()
                    elif guess_word=='hint' or guess_word=='Hint' or guess_word=='HINT':
                        os.system('cls')
                        print()
                        print(colour.yellow+'Your Out of Hints! -10 Points.'+colour.end)
                        score=score-10
                        print()
                        print(colour.cyan+'<-----Press Enter to Continue----->'+colour.end)
                        print()
                        input()
                    else:
                        os.system('cls')
                        print()
                        print(colour.red+'Incorrect! -10 Points, -1 Attempt.'+colour.end)
                        score=score-10
                        attempts_easy_difficulty=attempts_easy_difficulty-1
                        print()
                        print(colour.cyan+'<-----Press Enter to Continue----->'+colour.end)
                        print()
                        input()
                else:
                    os.system('cls')
                    print()
                    print(colour.red+'Incorrect! -10 Points, -1 Attempt.'+colour.end)
                    score=score-10
                    attempts_easy_difficulty=attempts_easy_difficulty-1
                    print()
                    print(colour.cyan+'<-----Press Enter to Continue----->'+colour.end)
                    print()
                    input()
            else:
                os.system('cls')
                print()
                print(colour.red+'Incorrect! -10 Points, -1 Attempt.'+colour.end)
                score=score-10
                attempts_easy_difficulty=attempts_easy_difficulty-1
                print()
                print(colour.cyan+'<-----Press Enter to Continue----->'+colour.end)
                print()
                input()
        if attempts_easy_difficulty==0:
            os.system('cls')
            final_attempts_number=attempts_easy_difficulty
            print()
            print(colour.cyan+'<-----'+colour.red+'Your Out of Attempts!'+colour.cyan+'----->'+colour.end)
            print()
            print(colour.blue+'Game Over!'+colour.end)
            print()
            print(colour.cyan+'<-----Press Enter to Continue----->'+colour.end)
            print()
            input()

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
        print()
        print('<-----Press Enter to Continue----->')
        print()
        input()
        os.system('cls')
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
                print()
                print('<-----Press Enter to Continue----->')
                print()
                input()
            elif guess_word=='skip' or guess_word=='Skip' or guess_word=='SKIP':
                os.system('cls')
                print()
                print('Question Skipped! -10 Points.')
                score=score-10
                print()
                print('<-----Press Enter to Continue----->')
                print()
                input()
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
                    print()
                    print('<-----Press Enter to Continue----->')
                    print()
                    input()
                elif guess_word=='skip' or guess_word=='Skip' or guess_word=='SKIP':
                    os.system('cls')
                    print()
                    print('Question Skipped! -10 Points.')
                    score=score-10
                    print()
                    print('<-----Press Enter to Continue----->')
                    print()
                    input()
                elif guess_word=='hint' or guess_word=='Hint' or guess_word=='HINT':
                    os.system('cls')
                    print()
                    print('Your Out of Hints! -10 Points.')
                    score=score-10
                    print()
                    print('<-----Press Enter to Continue----->')
                    print()
                    input()
                else:
                    os.system('cls')
                    print()
                    print('Incorrect! -10 Points, -1 Attempt.')
                    score=score-10
                    attempts_medium_difficulty=attempts_medium_difficulty-1
                    print()
                    print('<-----Press Enter to Continue----->')
                    print()
                    input()
            else:
                os.system('cls')
                print()
                print('Incorrect! -10 Points, -1 Attempt.')
                score=score-10
                attempts_medium_difficulty=attempts_medium_difficulty-1
                print()
                print('<-----Press Enter to Continue----->')
                print()
                input()
        if attempts_medium_difficulty==0:
            os.system('cls')
            final_attempts_number=attempts_medium_difficulty
            print()
            print('<-----Your Out of Attempts!----->')
            print()
            print('Game Over!')
            print()
            print('<-----Press Enter to Continue----->')
            print()
            input()
                    
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
        print()
        print('<-----Press Enter to Continue----->')
        print()
        input()
        os.system('cls')
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
                print()
                print('<-----Press Enter to Continue----->')
                print()
                input()
            elif guess_word=='skip' or guess_word=='Skip' or guess_word=='SKIP':
                os.system('cls')
                print()
                print('Question Skipped! -10 Points.')
                score=score-10
                print()
                print('<-----Press Enter to Continue----->')
                print()
                input()
            else:
                os.system('cls')
                print()
                print('Incorrect! -10 Points, -1 Attempt.')
                score=score-10
                attempts_hard_difficulty=attempts_hard_difficulty-1
                print()
                print('<-----Press Enter to Continue----->')
                print()
                input()
        if attempts_hard_difficulty==0:
            os.system('cls')
            final_attempts_number=attempts_hard_difficulty
            print()
            print('<-----Your Out of Attempts!----->')
            print()
            print('Game Over!')
            print()
            print('<-----Press Enter to Continue----->')
            print()
            input()
        
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
    
#End Of Game Summary and High Score:
os.system('cls')
print()
print('<-----Game Summary----->')
print()
print('Player Name: {}'.format(game_player_name))
print('Difficulty Played: {}'.format(game_difficulty_name))
print('Final Score: {}'.format(score))
print('Words Guessed: {}'.format(game_words_guessed))
print('Attempts Left: {}'.format(final_attempts_number))
score=str(score)
game_words_guessed=str(game_words_guessed)
file=open('D:/School/Python/Year 11 - Term 1 Assessment - 2025/Save Files/Latest Game Session/Player Name.txt','w')
file=file.write(game_player_name)
file=open('D:/School/Python/Year 11 - Term 1 Assessment - 2025/Save Files/Latest Game Session/Difficulty Played.txt','w')
file=file.write(game_difficulty_name)
file=open('D:/School/Python/Year 11 - Term 1 Assessment - 2025/Save Files/Latest Game Session/Final Score.txt','w')
file=file.write(score)
file=open('D:/School/Python/Year 11 - Term 1 Assessment - 2025/Save Files/Latest Game Session/Words Guessed.txt','w')
file=file.write(game_words_guessed)
file=open('D:/School/Python/Year 11 - Term 1 Assessment - 2025/Save Files/High Score.txt','r')
file=file.read()
file=str(file)
high_score=file
high_score=int(high_score)
score=int(score)
if high_score<score:
    score=str(score)
    print()
    print('You Beat Your High Score!')
    print()
    print('Old High Score: {}'.format(high_score)+' < '+'New High Score: {}'.format(score))
    file=open('D:/School/Python/Year 11 - Term 1 Assessment - 2025/Save Files/High Score.txt','w')
    file=file.write(score)
else:
    print()
    print("You couldn't Beat Your High Score, Bad Luck.")
    print()
    print('High Score: {}'.format(high_score)+' > '+"This Game's Score: {}".format(score))
score=int(score)
game_words_guessed=int(game_words_guessed)
if score<=60 and game_words_guessed==0:
    print()
    print("Maybe this Game isn't for You...")
    print()
    print('<-----Press Enter to Continue----->')
    print()
    input()
elif score>60 and game_words_guessed==0:
    print()
    print('Bad Luck! Try to get Further!')
    print()
    print('<-----Press Enter to Continue----->')
    print()
    input()
elif score>1000 and game_words_guessed>50:
    print()
    print('Wow! Amazing Work.')
    print()
    print('<-----Press Enter to Continue----->')
    print()
    input()
else:
    print()
    print('Well Done!')
    print()
    print('<-----Press Enter to Continue----->')
    print()
    input()

#Game Conclusion:
os.system('cls')
print()
print("<-----Thank You for Playing Mitch's Word Scramble Game!----->")
print()
print('Goodbye!')
print()
print('<-----Press Enter to Exit----->')
print()
input()
sys.exit()