with open('data/01.txt', 'w', encoding = 'utf-8') as file:
    file.write('Hello, Python!\n')
    for i in range(5):
        file.write(f'{i}일차 파이썬 공부 중\n')