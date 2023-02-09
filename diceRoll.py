
import random
import time

i = 0
Player1Points = 0
Player2Points = 0
Player1Tiebreaker = 0
Player2Tiebreaker = 0
Winner_Points = 0
user1 = "user1"
user2 = "user2"
Player1Points = 0
Player2Points = 0

def roll():

    points = 0

    die1 = random.randint(1,6)

    die2 = random.randint(1,6)

    dietotal = die1 + die2

    points = points + dietotal

    if dietotal % 2 == 0:
        points = points + 10

    else:
        points = points - 5

    if die1 == die2:
        die3 = random.randint(1,6)
        points = points +die3

    return(points)


for i in range(0,5):
    Player1Points += roll()
    print('After this round ',user1, 'you now have: ',Player1Points,' Points')
    time.sleep(1)
    Player2Points += roll()
    print('After this round ',user2, 'you now have: ',Player2Points,' Points')
    time.sleep(1)

if Player1Points == Player2Points:
    while Player1Tiebreaker == Player2Tiebreaker:


        Player1Tiebreaker = random.randint(1,6)
        Player2Tiebreaker = random.randint(1,6)

    if Player1Tiebreaker > Player2Tiebreaker:
        Player2Points = 0
    elif Player2Tiebreaker > Player1Tiebreaker:
        Player1Points = 0


if Player1Points>Player2Points:
    Winner_Points = Player1Points
    winner_User = user1
    winner = (Winner_Points, user1)
elif Player2Points>Player1Points:
    Winner_Points = Player2Points
    winner = (Winner_Points, user2)
    winner_User = user2

print('Well done, ', winner_User,' you won with ',Winner_Points,' Points')

winner = (Winner_Points,',',winner_User)
f = open('Winner.txt', 'a')
f.write(''.join(winner))
f.write('\n')
f.close()

