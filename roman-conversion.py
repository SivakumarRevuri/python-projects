
def roman_conversion(num):
    print(num)

#take input
while True:
    num = input('Enter a to convert to Roman: ')
    if num.isdigit():
        num = int(num)
        break
    print('Please enter a valid input!!!')
        
result = roman_conversion(num)