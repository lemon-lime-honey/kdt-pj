fruit_count = dict()

with open('data/fruits.txt', 'r') as fruit:
    while True:
        temp = fruit.readline().strip()
        if not temp: break
        if temp in fruit_count:
            fruit_count[temp] += 1
        else:
            fruit_count[temp] = 1

with open('data/04.txt', 'w') as result:
    for key, value in fruit_count.items():
        result.write(f'{key} {value}\n')