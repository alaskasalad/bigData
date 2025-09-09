import random

def flip1in3():
    while True:
        a = random.randint(0, 1)
        b = random.randint(0, 1)

        num = 2 * a + b
        if num == 3:
            continue
        return (num == 0)
