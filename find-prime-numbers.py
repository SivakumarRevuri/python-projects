"""
Next Prime Number - 
    Have the program find prime numbers until the user
    chooses to stop asking for the next 
"""


# print("Press enter to continue printing the number or print 'q' for stopping th execution")

# next = input()  # for starting puropse if user wants to continue or not
# if next == 'q':
#     exit()
    
# print("\n ---Prime Numbers---")

# for i in range(100):
#     for j in range(2, i+1):
#         if i != j and i % j == 0: 
#             break
#         elif i == j and i % j == 0:
#             next = input()
#             if next == 'q':
#                 exit()
#             print(f"{i}", end=', ')

#             break

# different approach
def is_prime(num: int) -> bool:
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                return False
        else:
            return True
    
# prime_lst = [i for i in range(10000) if is_prime(i)]
# print(prime_lst)
# print('First 10 primes are: ', prime_lst[0:10])

for i in range(1000):
    if is_prime(i):
        print(i, end=', ')
