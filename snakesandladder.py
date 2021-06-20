import random
current=0

def dice():
    value = random.randint(1, 6)
    print(value)
    return value

def game():
    while True:
            players=int(input("Enter the number of players:"))
            if players > 4:
                print("SORRY!!..only 4 people allowed")
            if players<2:
                print("SORRY!!..get a partner to play!!")
            else:
                break

    names = {}
    for i in range(1, players+1):
        while True:
            name = input("What is the name of Player {}? ".format(i))
            if not name in names:
                names[name] = 0
                break
    return names

def move(player, current):
    snake = {16: 2, 33: 12, 48: 34, 62: 36, 78: 69, 94: 8}
    ladder = {3: 15, 8: 25, 20: 56, 57: 63, 60: 77, 80: 98}

    throw = dice()
    next = current + throw
    print("{0} you got {1} you reached {2}".format(player, throw, next))

    if next in snake:
        print("AHH!!!..snakes...go to {}".format(snake[next]))
        next = snake[next]
    elif next in ladder:
        print("VOILA!!..u jumped to {}".format(ladder[next]))
        next = ladder[next]
    return next

def win(players):
    print("{}, LET'S START THE SNAKES AND LADDER ".format(" ".join(players)))
    input("Press Enter to Start")
    while True:
        for player, current in players.items():
            players[player] = move(player, current)
            if players[player]>100:
                return player
            input("***..pass the game..HIT ENTER..***")


players = game()
winner = win(players)
print("Player {} won the game".format(winner))