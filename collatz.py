

def collatz(number):
        
    while number != 1:
        if number % 2 == 0:
            number = number // 2
            print(number)
        else:
            number = 3 * number + 1
            print(number)

print('Enter number:')
try:
    number = int(input())
    collatz(number)
except ValueError:
    print('You  must use an integer')
