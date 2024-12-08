#Part 1
lst = [7, 8, 10]
lst2 = [7, 8, 10]
'''
Official Solution: lst is an alias
My Solution Correct
'''

#Part 2
lst = [4, 5, 6] #Outside lst (bc there is no call to function)
lst = [7, 8, 9, 7] #Inside func (if there was a call to function)

'''
Just outside is actually called so list of [4, 5, 6] is printed
Tracing the list inside func:   Changing from og list of [4, 5, 6] to point to a new list (parameter) [7, 8, 9,] which is appended to be [7,8,9,7]
'''

#Part 3
lst = [10, 2, [30, 1]]
lst_copy = [1, 2, [30, 1]]

'''
lst_copy -> Shallow copy that has diff container but points to same things
lst points to 1,2, and the list inside of , 2, 1
Shallow has new container but points to same things
lst is changed so it no longer points to 1, it points to 10
change in 10 is reflected in original, change for 30 is made to both 
'''

#Part 4
lst = [10, 2, [2, 1]]
lst_copy = [1, 2, [30, 1]]
'''
0 in first becomes 10
lst_copy changes from 2 to 30
'''