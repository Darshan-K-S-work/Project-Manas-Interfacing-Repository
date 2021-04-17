import time
import random

p1 = " "
p2 = " "

snakes = {
    21: 15,
    23: 6,
    29: 15,
    35: 18,
    47: 32,
    52: 38,
    71: 34,
    82: 59,
    95: 78,
    99: 79
}
ladders = {
    2: 18,
    11: 31,
    12: 28,
    22: 40,
    36: 62,
    41: 59,
    46: 55,
    70: 94,
    77: 84,
    85: 97
}
bite = ["~~~You just got bit!", "Snake bite!", "Look for First Aid!"]
climb = ["# You just found a ladder!", "Climb away!", "Nailed it!"]


def board(arr, num, k, l):  # Print the board template
    count = 0

    for m in range(2, 39, 4):
        arr.append(int(m))

    for b in range(100, 90, -1):
        num.append(int(b))
    for b in range(81, 91):
        num.append(int(b))
    for b in range(80, 70, -1):
        num.append(int(b))
    for b in range(61, 71):
        num.append(int(b))
    for b in range(60, 50, -1):
        num.append(int(b))
    for b in range(41, 51):
        num.append(int(b))
    for b in range(40, 30, -1):
        num.append(int(b))
    for b in range(21, 31):
        num.append(int(b))
    for b in range(20, 10, -1):
        num.append(int(b))
    for b in range(1, 21):
        num.append(" "+str(b))

    for i in range(10):
        for j in range(41):
            if (j % 4 == 0):
                print(" | ", end=" ")
            elif (j in arr):
                print(num[count], end=" ")
                count += 1
        print("\n")
    print("-"*45)
    print("Snakes present at:\n", k)
    print("Ladders present at:\n", l, "\n")
    print("-"*45)

def dice():  # Returns Dice roll value
    return random.randint(1, 6)


def play(chance, p1, p2, p1pos, p2pos, d, k, l, bite, climb):  # Main gameplay
    while(not(p1pos == 100) or not(p2pos == 100)):
        if (chance == 1):
            print("\n"+p1+"\'s chance.")
        elif (chance == 2):
            print("\n"+p2+"\'s chance.")

        input("Press Enter to roll the dice")
        print("Rolling dice...")
        time.sleep(2)
        d = dice()
        print("It\'s a "+str(d))

        if (chance == 1):
            p1pos = p1pos + d
            if (p1pos > 100):  # Dice takes you beyond 100
                print("Shoot! You were off by a bit.")
                p1pos = p1pos - d
            if (p1pos == 100):
                break
            print("Moving...")
            time.sleep(2)
            print("\n"+p1+" is at square "+str(p1pos))
        else:
            p2pos = p2pos + d
            if (p2pos > 100):  # Dice takes you beyond 100
                print("Shoot! You were off by a bit.")
                p2pos = p2pos - d
            if (p2pos == 100):
                break
            print("Moving...")
            time.sleep(2)
            print("\n"+p2+" is at square "+str(p2pos))

        if (chance == 1):
            if (p1pos in k):  # Landed on a snake head
                time.sleep(1)
                print("\a"+bite[random.randint(0, 2)])
                p1pos = snakes[p1pos]
                print("You were sent down to box "+str(p1pos)+"\n")
            elif (p1pos in l):  # Landed on foot of ladder
                time.sleep(1)
                print("\a"+climb[random.randint(0, 2)])
                p1pos = ladders[p1pos]
                print("You climbed up to box "+str(p1pos)+"\n")
            chance = 2
        else:
            if (p2pos in k):  # Landed on a snake head
                time.sleep(1)
                print("\a"+bite[random.randint(0, 2)])
                p2pos = snakes[p2pos]
                print("You were sent down to box "+str(p2pos)+"\n")
            elif (p2pos in l):  # Landed on foot of ladder
                time.sleep(1)
                print("\a"+climb[random.randint(0, 2)])
                p2pos = ladders[p2pos]
                print("You climbed up to box "+str(p2pos)+"\n")
            chance = 1

        time.sleep(2)
        print("-"*35)
        if (p1pos > p2pos):
            print("\t"+str(p1)+" is leading!")
        elif (p1pos < p2pos):
            print("\t"+str(p2)+" is leading!")
        else:
            print("\tBoth are on the same Box!")
        print("-"*35)

    # Outside while => Someone Won
    if(p1pos == 100):
        print("\n")
        print("-"*70)
        print("\a\t\t\t"+str(p1)+" Won the Game!!!")
        print("\t\t\t"+p1+" Congratulations!")
        print("-"*70)
    elif(p2pos == 100):
        print("\n")
        print("-"*70)
        print("\a\t\t\t"+str(p2)+" Won the Game!!!")
        print("\t\t\t"+p2+" Congratulations!")
        print("-"*70)
