# Problem 1: Simple Stuff

data = [8, 2, -4, 28, 4, 31]
start = 1
end = 6

'''
1. data[1] = 2
2. data[-3] = 28
3. data[end-1*2] = 4
4. data[6] indexError

5. data.append(12) = [8, 2, -4, 28, 4, 31, 12]
6. daya.extend(13) error
7. data.extend([5,3, 1]) = [8, 2, -4, 28, 4, 31, 5, 3, 1]
8. data.insert("foo", 3) = error
9. data.remove(-4) = [8, 2, 28, 4, 31, 12, 5, 3, 1]
10. data.insert(start, end) = [8, 6, 2, 28, 4, 1, 5, 3, 1]
11. data.append([1, 3, 5]) = [8, 2, -4, "foo", 28, 4, 1, 5, 3, 1, [1, 3, 5]]
'''

# Problem 2: lowercase function 

def lower(lst):
    lower = []
    length = len(lst)

    for ind in range(length):
        temp = lst[ind].lower()
        lower.append(temp)
    return lower

def main():
    data = ['CAt', 'DoG', 'GoAT', 'DuCk']
    lower_list = lower(data)
    print(lower_list)

main()
