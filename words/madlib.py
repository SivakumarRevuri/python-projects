name = input('noun: ')
dynasty = input('dynasty: ')
# verb1 = input('verb1: ')
# verb2 = input('verb2: ')
# adjective1 = input('adjective1: ')

print('Once upon a there is a king named '+name+' belong to: '+dynasty+' dynasty')
print('Once upon a there is a king named {} belong to: {} dynasty'.format(name, dynasty))
#or
madlib = f'Once upon a there is a king named {name} belong to: {dynasty} dynasty'
print(madlib)

#since this is a function, dev don't have to pass self here
def test():
    print('test')
    
test()