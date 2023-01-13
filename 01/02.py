with open('data/fruits.txt', 'r') as fruit:
    lines = len(fruit.readlines())

with open('data/02.txt', 'w') as result:
    result.write(str(lines))