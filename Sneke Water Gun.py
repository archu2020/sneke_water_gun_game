import random
print("SNAKE WATER GUN GAME\n")

print("s for Sneke")
print("w for Water")
print("g for Gun\n")

chance = 10
no_of_chance = 0
User_point = 0
Computer_point = 0

while (no_of_chance<10):
    choices = ["s", "w", "g"]
    print("Please chose s for Sneke , w for Water and g for Gun")
    a = str(input())
    b = random.choice(choices)
    if a == b:
        print("Draw, no point given")
        print(f"Computer points are {Computer_point} AND Yours points are {User_point}")


    elif a == "s" and b == "g":
        print(f"Computer chose Gun, so Computer won")
        Computer_point += 1
        print(f"Computer points are {Computer_point} AND Yours points are {User_point}")


    elif a == "s" and b == "w":
        print(f"Computer chose water, so You won, 1 point has been given")
        User_point += 1
        print(f"Computer points are {Computer_point} AND Yours points are {User_point}")


    elif a == "w" and b == "g":
        print(f"Computer chose Gun, so You won, 1 point has been given")
        User_point += 1
        print(f"Computer points are {Computer_point} AND Yours points are {User_point}")


    elif a == "w" and b == "s":
        print(f"Computer chose Sneke, Coumputer You won, 1 point has been given")
        Computer_point += 1
        print(f"Computer points are {Computer_point} AND Yours points are {User_point}")


    elif a == "g" and b == "s":
        print(f"Computer chose Sneke, so You won, 1 point has been given")
        User_point += 1
        print(f"Computer points are {Computer_point} AND Yours points are {User_point}")


    elif a == "g" and b == "w":
        print(f"Computer chose Gun, Coumputer You won, 1 point has been given")
        Computer_point += 1
        print(f"Computer points are {Computer_point} AND Yours points are {User_point}\n")



    elif a != choices:
        print("invalid input, please try again")

    no_of_chance = no_of_chance + 1
    print(f"{chance - no_of_chance} chance is left out of {chance} chance\n")

    if no_of_chance == 10:
        print("Your total Score is",User_point)
        print("Computer total Score is", Computer_point)
        if User_point == Computer_point:
            print("Game DRAW!!")
        elif User_point > Computer_point:
            print("Congrets!! You won!! By", User_point - Computer_point,"points")
        else:
            print(f"You Lose!! By", Computer_point - User_point, "Batter Luck next time\n")
        print("Thank you for playing this game")





