# import cs50 becouse it's easier to receive data input
import cs50


def main():
    # data input
    while (True):
        h = cs50.get_int("Height: ")
        if h >= 1 and h != 9:
            break
    i = h - 1
    z = 1
    # our output
    for j in range(h):
        print(" " * i + "#" * z)
        i -= 1
        z += 1


if __name__ == "__main__":
    main()
