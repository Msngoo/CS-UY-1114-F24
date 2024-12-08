list = ['apple', 'banana',['orange', 'grape']]
shallowCopy = list[:]
shallowCopy[2][0] = 'kiwi'

print('Fruits:', list)
print('Shallow Fruits:', shallowCopy)