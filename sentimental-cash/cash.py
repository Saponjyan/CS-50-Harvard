# import cs50 becouse it's easier to receive data input
import cs50

# data input and immediately prepare for conversion to an integer
while (True):
    cents = (cs50.get_float("Change owed: ")) * 100
    if cents >= 0:
        break
a = 0
a += int(cents / 25)
b = int(cents % 25)
a += int(b / 10)
b = int(b % 10)
a += int(b / 5)
b = int(b % 5)
a += b
print(a)