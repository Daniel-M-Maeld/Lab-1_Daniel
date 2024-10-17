import time
SET_COLOR = "\x1b[48;5;"
END = "\x1b[0m"


def draw_line(offset=0, length=1, color=222):
    line = ' ' * length
    print(f"{' ' * offset}{SET_COLOR}{color}m{line}{END}")

if __name__ == "__main__":
    print()
    print("1)")
    print(f" \u001b[47m {' ' * 18} {END}")
    print(f" \u001b[47m {' ' * 18} {END}")
    draw_line(1,20,197)
    draw_line(1,20,197)
    print()
    print("2)")
    draw_line(1,15,231)
    draw_line(8,1,231)
    draw_line(1,15,231)
    print(f"    \u001b[48;5;231m {END}       \u001b[48;5;231m {END}")
    draw_line(1,15,231)

    print()
    print("3)")
    
    for i in range(9, 0, -1):
        x = 0  
        while x**0.5 <= i:
            print(f"{' ' * x}{SET_COLOR}231m {END}", end = "")
            print(f'\u001b[{x+1}D', end = "")
            x +=1
        print()

    print()
    print("4)")
    print()

    file = open("sequence.txt", 'r')

    sum = 0

    for i in range(125):
        sum += abs(float (file.readline()))
    
    print('Среднее по модулю первых 125 чисел: ', sum/125)

    sum = 0

    for i in range(125, 250):
        sum += abs(float (file.readline()))

    print('Среднее по модулю вторых 125 чисел: ', sum/125)
    
    file.close()
