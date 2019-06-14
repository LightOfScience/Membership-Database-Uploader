import random

numeric = ('0' , '1' , '2' , '3' , '4' , '5' , '6' , '7' , '8' , '9')
character = ('A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z')

choice = (numeric + character)

# Membership Number is 5 digit
def RandomID():
    d1 = random.choice(numeric)
    d2 = random.choice(numeric)
    d3 = random.choice(character)
    d4 = random.choice(character)
    d5 = random.choice(choice)

    MemberID = [d1 , d2 , d3 , d4 , d5]
    random.shuffle(MemberID)
    MemberID = ''.join(MemberID)

    return MemberID