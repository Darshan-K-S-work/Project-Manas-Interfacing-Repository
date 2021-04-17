# Reset the high score to 0


print("Are you sure you want to reset high score?(0/1): ")
if(int(input()) == 1):
    f = open("high_score.txt", "w")
    f.write("0")
    f.close()
    print(">Success")
    input()
