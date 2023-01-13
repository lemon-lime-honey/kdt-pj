import json

form = ['id', 'title', 'vote_average', 'overview', 'genre_ids']

# 아래 코드 수정 금지
movie_json = open("data/movie.json", encoding="UTF8")
movie = json.load(movie_json)

# 이하 문제 해결을 위한 코드 작성
for item in form:
    for key, value in movie.items():
        if key == item:
            print(f'{key}: {value}')