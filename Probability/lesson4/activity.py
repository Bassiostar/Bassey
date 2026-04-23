def find_prob(a,b):
    if a == 1:
        prob_a = 0.2
        if b == 2:
            prob_bga = 0.85
        elif b == 2:
            prob_bga = 0.15
        else:
            print("Invalid Choice")
        prob_a_and_b = prob_a * prob_bga
        print("The probability of B given A is: ", prob_bga)
        print("The probability of both events occurring is: ", prob_a_and_b)

    elif a == 2:
        prob_a = 0.8
        if b == 1:
            prob_bga = 0.02
        elif b == 2:
            prob_bga = 0.98
        else:
            print("Invalid Choice")
        prob_a_and_b = prob_a * prob_bga
        print("The probability of B given A is: ", prob_bga)
        print("The probability of both events occurring is: ", prob_a_and_b)

    else:
        print("Invalid Choice")

print("Let's calculate probability. Please enter choices for the events...")

print("Person has step throat? \n 1. Yes \n 2. No")
a = int(input("Enter your choice (1 / 2): "))

print("Person has tested positive? \n 1. Yes \n 2. No")
b = int(input("Enter your choice (1 / 2): "))

print("Probabilities for event a and b: ")
find_prob(a, b)