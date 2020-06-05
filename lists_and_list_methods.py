import copy
listOne = ['Red', 'Wizard', 'Hat']

#append
listOne.append('Rules')
print(listOne)

#clear
listOne.clear()
print(listOne)

#copy (hint: you need two string variables)
listTwo = []
listTwo = copy.copy(listOne)
print(listOne)
print(listTwo)

#count
print(listOne.count('Wizard'))

#extend
listTwo = ['Rules', 'The', 'Roost']
listOne.extend(listTwo)
print(listOne)

#index (use twice, once for an item in the list, once for an item not in the list)
print(listOne.index('Hat'))
print(listOne.index('Black'))

#insert
listOne.insert(2, 'Conical')
print(listOne)

#remove
listOne.remove('Wizard')
print(listOne)

#reverse
print(listOne)
listOne.reverse()
print(listOne)

#sort
listOne.sort()
print(listOne)
