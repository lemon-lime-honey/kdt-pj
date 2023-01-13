import json

form = ['id', 'title', 'poster_path', 'vote_average', 'overview', 'genre_ids']

# 아래 코드 수정 금지
movies_json = open("data/movies.json", encoding="UTF8")
movies_list = json.load(movies_json)

# 이하 문제 해결을 위한 코드 작성
for movie in movies_list:
    for item in form:
        for key, value in movie.items():
            if key == item:
                print(f'{key}: {value}')
                break
    print()