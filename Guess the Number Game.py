print("**************** Guess The Number Game **********************")
print("You have only 5 chances")

guess = 5
master = 25
for i in range(1, 6):
    key = int(input("Enter your choice: "))
    left = guess - i
    if left == 0:
        print("Sorry, you don't have any guesses left. Play Again!!")
        break
    else:
        if key > master:
            print("You entered a greater number kindly reduce it.")
            print("You have only", left, "guesses left.")
            continue
        elif key < master:
            print("You have lesser number kindly increase it.")
            print("You have only", left, "guesses left.")
            continue
        else:
            print("Hurrah!! You have guessed a correct number i.e.", master)
            break

