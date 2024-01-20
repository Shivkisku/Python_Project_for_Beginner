import random

num = random.randrange(1000, 10000)

n = int(input("Guess the 4-digit number:"))

if n == num:
    print("Great! You guessed the number in just 1 try! You're a Mastermind!")
else:
    ctr = 0

    while n != num:
        ctr += 1
        count = 0

        n_str = str(n)
        num_str = str(num)

        correct = ['X'] * 4

        for i in range(4):
            if n_str[i] == num_str[i]:
                count += 1
                correct[i] = n_str[i]

        print("Not quite the number. But you did get ", count, " digit(s) correct!")

        # Print the correct digits (uncomment if needed)
        # print("Also these numbers in your input were correct:")
        # for k in correct:
        #     print(k, end=' ')

        print('\n')
        print('\n')
        n = int(input("Enter your next choice of numbers: "))

        # When none of the digits are guessed correctly.
        if count == 0:
            print("None of the numbers in your input match.")
            n = int(input("Enter your next choice of numbers: "))

    # Condition for equality.
    if n == num:
        ctr += 1
        print("You've become a Mastermind!")
        print("It took you only", ctr, "tries.")
