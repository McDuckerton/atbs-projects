def collatz(number):
    if number % 2 == 0:
        return number // 2
    else:
        return 3 * number + 1

if __name__ == "__main__":

    try:
        num = int(input('Please enter a number here: '))
        result = collatz(num)
        while(result != 1):
            result = collatz(result)
            print(result)
    
    except ValueError:
        print('This was not right, please try again with a valid number.')

