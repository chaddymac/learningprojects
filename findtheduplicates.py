# Exercise: Check for duplicates in list

new_list = input('Create a new list separated by spaces:')

#seperating the listed items

list_split = (new_list.split())
duplicates = []
print(list_split)
for name in list_split:
  if list_split.count(name) > 1:
    if name not in duplicates:
      duplicates.append(name)
print(duplicates)