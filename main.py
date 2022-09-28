keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

# define a dictionary
dictionary = {}

for i in range(len(keys)):
    dictionary.update({keys[i]: values[i]})
 #update method inserts the specified items to dictionary

print(dictionary)
