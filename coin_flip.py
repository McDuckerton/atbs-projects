import random

def coin_flip_streaks():
    
    count = 0
    check = None
    current = None
    streaks = 0
    for a in range(10000):
        coin_list = []
        for i in range(100):
            n = random.randint(0,1)
            if n == 0:
                coin_list.append('h')
            elif n == 1:
                coin_list.append('t')
        for j in range(len(coin_list)):
            current = check
            check = coin_list[j]
            if current == check:
                count += 1
            else: 
                count = 0

            if count == 6:
                streaks += 1
        
        return streaks

if __name__ == '__main__':
    result = coin_flip_streaks()
    print('Chances of streak: %s%%' % (result / 100))





