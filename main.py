text = 'Google создаст 10 специальную команду для поиска 15 багов в особо важных приложениях. 23'
lists = text.split()
numbers = []
letters = []

for i in lists:
    if i.isdigit():
        numbers.append(i)

    else:
        letters.append(i)

print(numbers)
print(letters)
print("hello Git")
