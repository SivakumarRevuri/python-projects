def binary_search(lst, value):
    #base case here
    if len(lst) == 1:
        return lst[0] == value

    mid = int(len(lst)/2)
    if lst[mid] < value:
        return binary_search(lst[:mid], value)
    elif lst[mid] > value:
        return binary_search(lst[mid+1:], value)
    else:
        return True

lst = [1,2,3,4,5,6,9]
mid = int(len(lst)/2)
value = 8 # value to find
res = 0
if lst[mid] > value:
    res = binary_search(lst[:mid], value)
elif lst[mid] < value:  
    res = binary_search(lst[mid+1:], value)
print(res)