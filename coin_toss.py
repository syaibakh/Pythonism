import random

coin = ["head","tail"]
toss = random.choice(coin)
select = input("Head or Tail?: ").lower
if select == toss and select in coin:
        print("You Win !!!")
elif select != toss and select in coin:
    print("You Lost !!!")
else:
    print("Please enter Head or Tail!!!")
#Need to fix...