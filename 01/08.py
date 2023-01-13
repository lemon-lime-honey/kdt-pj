import json

form = ['id', 'title', 'vote_average', 'overview']
genre = list()

# 아래 코드 수정 금지
movie_json = open("data/movie.json", encoding="UTF8")
movie = json.load(movie_json)

genres_json = open("data/genres.json", encoding="UTF8")
genres_list = json.load(genres_json)

# 이하 문제 해결을 위한 코드 작성
for item in form:
    for key, value in movie.items():
        if key == item:
            print(f'{key}: {value}')
            break

for item in movie['genre_ids']:
    for temp in genres_list:
        if item == temp['id']:
            genre.append(temp['name'])

print('genre_names: ', genre)