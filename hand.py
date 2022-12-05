# player deck

shapes = {'♠': 0 , '♦':0 , '♥':0, '♣':0 }
values = {'A':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0,'10':0,'J':0,'Q':0,'K':0}
num = ''
shape = ''

def clearall():
    global shapes
    global values
    global num
    global shape

    shapes = {'♠': 0 , '♦':0 , '♥':0, '♣':0 }
    values = {'A':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0,'10':0,'J':0,'Q':0,'K':0}
    num = ''
    shape = ''


def checking(deck):

    for cards in deck:

        if len(cards) == 2:
            shapes[cards[0]] += 1
            values[cards[1]] += 1

        elif len(cards) == 3:
            shapes[cards[0]] += 1
            values[cards[1:]] += 1

def flush():
    global shape

    for k, v in shapes.items():
        if v >= 5:
            shape = k
            return True, values
    else: 
        return False

def straight(deck):
    count = 0
    value = []
    
    for cards in deck:
        if len(cards) == 2:
            num = cards[1]
            if num == 'A':
                num = 14
                value = value + [int(num)]
            elif num == 'J':
                num = 11
                value = value + [int(num)]
            elif num == 'Q':
                num = 12
                value = value + [int(num)]
            elif num == 'K':
                num = 13
                value = value + [int(num)]
            else:
                value = value + [int(num)]
        else:
            num = cards[1:]
            value = value + [int(num)]
    
    value.sort()

    for i in range(len(value)-2):
        
        if int(value[i]) == int(value[i+1]) - 1:
                count += 1
    
    if count >= 5:
        return True, value
    else:
        return False, value

def royal(deck):
    check = straight(deck)
    list = check[1]
    
    if True in check:
        if 10 and 11 and 12 and 13 and 14 in list:
            return True
        else:
            return False
    else:
        return False

def royalFlush(deck):
    fp = flush()
    sp = royal(deck)
    if fp and sp:
        return True
    else:
        return False

def straightFlush(deck):
    fp = flush()
    sp = straight(deck)

    if fp == True and sp == True:
        return True
    else:
        return False

def fourOfKind(deck):
    global num

    for k, v in values.items():
        if v == 4:
            num = k
            return True
    else:
        return False

def fullHouse(deck):
    count = 0
    global num
    for k, v in values.items():
        if v == 3:
            num += k
            count += 3

        elif v == 2:
            num += k
            count +=2
    
    if count == 5:
        return True

    else:
        num = ''
        return False
              
def threeOfKind(deck):
    global num

    for k, v in values.items():
        if v == 3:
            num =  k
            return True
    return False

def twoPair(deck):
    global num

    count = 0
    for k, v in values.items():
        if v == 2:
            num +=  k + ' '
            count += 1

    if count == 2:
        
        return True
    else:
        return False

def pair(deck):
    global num
    count = 0
    for k, v in values.items():
        if v == 2:
            num = k
            count += 1
    if count == 1:
        return True
    else:
        return False

def checks(deck):
    deck = deck[:-1]
    deck = deck.split()

    score = 0

    checking(deck)
    
    if royalFlush(deck):
        score = 10
        return score

    elif straightFlush(deck):
        score = 9
        return score


    elif fourOfKind(deck):
        score = 8
        return score


    elif fullHouse(deck):
        score = 7
        return score

    elif flush():
        score = 6
        return score

    elif straight(deck) == True:
        score = 5
        return score

    elif threeOfKind(deck):
        score = 4
        return score


    elif twoPair(deck):
        score = 3
        return score


    elif pair(deck) == True:
        score = 2
        return score

    else:
        for i in deck:
            if i == 'A':
                i = 14
            elif i == 'J':
                i = 11
            elif i == 'Q':
                i = 12
            elif i == 'K':
                i = 13
        deck.sort()
        maxi = max(deck)
        
        if maxi == 14:
            maxi = 'A'
        elif maxi == 11:
            maxi = 'J'
        elif maxi == 12:
            maxi = 'Q'
        elif maxi == 13:
            maxi = 'K'

        score = 1
        return score, maxi


def result(deck):
    global num
    global shape

    score = checks(deck)

    if score == 10:
        return("{} royal flush ".format(shape), score) 

    elif score == 9:
  
        return("{} straight flush".format(shape), score)

    elif score == 8:
        
        return("{} four of kind".format(num), score)

    elif score == 7:
        
        return("{} , {} full house".format(num[0], num[1]), score)

    elif score == 6:
        
        return("{} flush".format(shape), score)

    elif score == 5:
        
        return("{} straight".format(deck), score)

    elif score == 4:
        
        return("{} tree of kind".format(num), score)

    elif score == 3:
        num = num.split(" ")
        return("{},{} two pair".format(num[0],num[1]), score)

    elif score == 2:
        
        return("{} one pair".format(num), score)
        
    else:
        
        return("{} high card".format(score[1]), score)

    