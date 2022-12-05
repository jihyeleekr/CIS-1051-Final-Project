# Jihye Lee CIS 1051
import random

deck = ['♠A','♠2','♠3','♠4','♠5','♠6','♠7','♠8','♠9','♠10','♠J','♠Q','♠K','♦A','♦2','♦3','♦4','♦5','♦6','♦7','♦8','♦9','♦10','♦J','♦Q','♦K','♥A','♥2','♥3','♥4','♥5','♥6','♥7','♥8','♥9','♥10','♥J','♥Q','♥K','♣A','♣2','♣3','♣4','♣5','♣6','♣7','♣8','♣9','♣10','♣J','♣Q','♣K']
comdeck = ''
chips = 100000
pot = 0
ante = 0
playerdeck = ''
dealerdeck = ''
comdeck = ''


def clearall():
    global ante
    global pot
    global comdeck
    global deck
    global playerdeck
    global dealerdeck

    ante = 0
    pot = 0
    comdeck = ''
    deck = ['♠A','♠2','♠3','♠4','♠5','♠6','♠7','♠8','♠9','♠10','♠J','♠Q','♠K','♦A','♦2','♦3','♦4','♦5','♦6','♦7','♦8','♦9','♦10','♦J','♦Q','♦K','♥A','♥2','♥3','♥4','♥5','♥6','♥7','♥8','♥9','♥10','♥J','♥Q','♥K','♣A','♣2','♣3','♣4','♣5','♣6','♣7','♣8','♣9','♣10','♣J','♣Q','♣K']
    playerdeck = ''
    dealerdeck = ''

def suffle():
    deck = deck.shuffle()
    return deck

def start():
    global chips
    global ante
    global pot
    play = input("Do you want to start a hand? \n1) Ante \n2) Fold \n")
    
    print()

    if play == '1':
        print("How much will you bet?")
        print("You have {} chips".format(chips))
        print()

        ante = int(input("Enter the amount of chip(s): "))
        pot = pot + ante
        if ante == chips:
                print("ALL IN!")
                print("Good Luck")
                chips = chips - ante
        else:
            chips = chips - ante
            print()
            print("{} chip(s) are left".format(chips))
            print()
        

    elif play == '2' :
        print("See you next time~")
        exit()

    else:
        print("{} is not a valid option. Please try again.".format(play))
        poker()

def end():
    print("Do you want to play again? (Y/N)")
    user = input(' ')

    if user =='Y' or user == 'y':
        clearall()
        poker()

    elif user =='N' or user =='n':
        print("It was a great game! \n See you next time!")
        exit()

    while user != 'Y' or user != 'y' or user != 'N' or user != 'n':
        print('That is not a valid input \n Please try again.')
        end()

def playerHolds():
    global playerdeck
    for _ in range(2):
        result = random.choice(deck)
        playerdeck += result + ' '
        deck.remove(result)
    print(playerdeck) 

def dealerHolds():
    global dealerdeck
    for _ in range(2):
        result = random.choice(deck)
        dealerdeck += result + ' '
        deck.remove(result)
    return playerdeck

def comDeck(n):
    global comdeck
    global playerdeck
    global dealerdeck

    for _ in range(n):
        result = random.choice(deck)
        playerdeck +=  result +  ' '
        dealerdeck +=  result +  ' '
        comdeck = comdeck + ' ' + result
        deck.remove(result)

    print(comdeck)

def bet():
    global bets
    bets = int(input('Enter the amount of chips: '))
    print()

def deal1():
    global chips
    global pot
    global ante
    global bets

    play = input("1) Fold  2) Bet \n")
    print()

    if play == '1':
        print("You lost", pot, 'chip(s)')
        clearall()
        poker()
    
    elif play == '2':
        print('You should bet twice amount of your ante bet.')
        print('It will be', ante *2, 'chips.')
        print()
            
            #betting
        bet()

        while bets != ante * 2 or bets > chips :
            print('You should bet the same amount as ante bet.')
            print()
            print('You currently have', chips, 'chip(s).')
            print()
            print('It will be', ante *2, 'chip(s).')
            print()
            bet()

        if bets == chips or bets == ante * 2:    
            #amount of chips
            chips = chips - bets
            
            if chips == 0:
                print("ALL IN!")
                print("Good Luck")
            
            print(chips, "chip(s) are left")
            print()
            comDeck(3)
            print()
            print('Your deck is:', playerdeck[0:6])
            pot = pot + bets
            print()
            print("Current pot is",pot, 'chip(s)')
            print()
    else:
        print(play, "is not valid option. Please try again.")
        deal1()
        
def deal2():
    global bets
    global chips
    global pot
    global ante

    play = input("1) Check 2) Fold  3) Bet \n")

    print()

    if play == '1' :
        comDeck(1)
        print()
        print('Your deck is:', playerdeck[0:6])
        print()
        print("Current pot is",pot)
        print()

    elif play == '2':
        print()
        print("You lost", pot, 'chips')
        clearall()
        poker()

    elif play == '3' or play =="bet":
            
        print()
        print('You should bet the same amount as ante bet.')
        print('It will be', ante , 'chip(s).')
        print()

        bet()

        while bets != ante or bets > chips :
            print('You should bet the same amount as ante bet.')
            print()
            print('You currently have', chips, 'chip(s).')
            print()
            print('It will be', ante, 'chip(s)')
            print()
            bet()
    
        if bets == chips or bets == ante:
            chips = chips - bets
            if chips <= 0:
                print("ALL IN!")
                print("Good Luck")
            
            print(chips, "chip(s) are left")
            print()
            comDeck(1)
            print()
            print('Your deck is:', playerdeck[0:6])
            print()
            pot = pot + bets

            print("Current pot is",pot)
            print()
    else:
        print(play, "is not valid option. Please try again.")
        deal2()

def poker():
    global chips
    global pot
            
    start()

    playerHolds()

    dealerHolds()
#Flop
    deal1()
#Turn & River
    for _ in range(2):
        deal2()

    print("playerdeck is:", playerdeck , "dealerdeck is:", dealerdeck)
    
    from hand import result, clearall

    clearall()
    phand = result(playerdeck)
    player = phand[1]
    clearall()
    dhand = result(dealerdeck)
    dealer = dhand[1]
    print(type(player),type(dealer))

    if player > dealer:

        print("Your hand is {}".format(phand[0]), end = ' ')
        print("Dealer's hand is {}".format(dhand[0]))
        chips += pot
        print("You Win!")

    elif dealer > player:

        print("Your hand is {}".format(phand[0]), end = ' ')
        print("Dealer's hand is {}".format(dhand[0]))
        print("Dealer Win!")

    else:
        print("Your hand is {}".format(phand[0]), end = ' ')
        print("Dealer's hand is {}".format(dhand[0]))
        print("DRAW")
    
    end()


poker()