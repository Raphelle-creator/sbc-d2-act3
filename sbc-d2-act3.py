import random

user_input = input("Enter your bet (three integers separated by spaces): ")
bet = [int(num) for num in user_input.split()]

if len(bet) != 3:
    print("Please enter exactly three integers.")
else:
    result = [random.randint(0, 9) for _ in range(3)] 
    print(f"Result: {result}")

    if bet == result:
        print("You Win!")
    elif sorted(bet) == sorted(result):
        print("You Partially Win!")
    else:
        print("You Lose!")