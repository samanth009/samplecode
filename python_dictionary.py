#Adding a key to dictionary
d = {1:3, 6:10}
print(d)
d.update({5:15, 2:8})
print(d)

#Merging two dictionaries into one
d1 = {1:3, 6:10}
d2 = {5:15, 2:8}
d = d1.copy()
d.update(d2)
print(d)