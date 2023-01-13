fruit_list = list()

with open('data/fruits.txt', 'r') as fruit:
    while True:
        temp = fruit.readline().strip()
        if not temp: break
        if temp[-5:] == 'berry':
            if temp in fruit_list:
                continue
            else:
                fruit_list.append(temp)

with open('data/03.txt', 'w') as result:
    result.write(str(len(fruit_list)) + '\n')
    for item in fruit_list:
        result.write(item + '\n')