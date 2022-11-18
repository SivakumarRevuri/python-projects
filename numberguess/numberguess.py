import random 

def guess(value):
    random_num = random.randint(1,value)
    guess = 0
    while guess != random_num:
        guess = int(input('enter your number: '))
        if guess < random_num:
            print('Sorry! guess agian, it is too low')
        elif guess > random_num:
            print('Sorry! guess agian, it is too high')
    print('Congrats! you got a reward ', random_num)
    return random_num

def find_num_ai(num):
    random_number = 0
    count = 0
    min, max = 1, 10
    while num != random_number:
        random_number = random.randint(min, max)
        count +=1
        if num < random_number:
            print('Sorry! guess agian, it is too low')
            max +=1
        elif num > random_number:
            print('Sorry! guess agian, it is too high')
            min +=1
    print('great! AI guessed the', random_number,' in ', count, 'th attempt')

# guess(value=10)
num = int(input('enter a number in the range 1 to 10: '))
find_num_ai(num=num)