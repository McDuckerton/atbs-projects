def collatz(number):
    if number % 2 == 0:
        return number // 2
    else:
        return 3 * number + 1

if __name__ == "__main__":

    try:
        num = int(input('Enter your number: '))
        result = collatz(num)
        while(result != 1):
            result = collatz(result)
            print(result)
    
    except ValueError:
        print('Please enter a valid number.')

