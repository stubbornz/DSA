from random import randint

sum = 20000
bet = 500
loss = 0
profit = 0
chance = 0

sleact = int(input("Enter your Dice sleaction"))

while(sum >= 0):
    profit = 0
    chance += 1
    x = randint(2, 12)
    print("Bet = ", bet)
    if x == sleact:
        sum = sum + (bet * 3)
        profit = profit + (bet*3)
        bet = 500

    else:
        loss = loss + bet
        sum = sum - bet
        bet = bet + 500

    print("Chances = ", chance)
    print("Dice = ", x)
    print("Total = ", sum)
    print("Loss = ", loss)
    print("Profit = ", profit)
    print("Total profit = ", profit - loss)

    input()
