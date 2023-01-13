import requests, os
from dotenv import load_dotenv
from pprint import pprint

def credits(title):
    load_dotenv()
    url = f'https://api.themoviedb.org/3/'
    api_key = os.getenv("tdmb_api")
    params = {'api_key': api_key, 'language': 'ko-KR', 'query': title, 'region': 'KR'}

    movieinfo = requests.get(url = url + 'search/movie', params = params).json()
    results = movieinfo['results']

    try:
        target = results[0]['id']
    except:
        target = None

    if target:
        params = {'api_key': api_key, 'language': 'ko-KR'}
        temp = requests.get(url = url + f'movie/{target}/credits', params = params).json()
        res = {'cast': [], 'crew': []}

        for cast in temp['cast']:
            if cast['cast_id'] < 10:
                res['cast'].append(cast['name'])
        for crew in temp['crew']:
            if crew['department'] == 'Directing':
                res['crew'].append(crew['name'])
        return res
    else:
        return None

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화 id를 통해 영화 상세정보를 검색하여 주연배우 목록(cast)과 스태프(crew) 중 연출진 목록 반환
    영화 검색에 실패할 경우 None을 반환
    """
    pprint(credits('기생충'))
    # {'cast': ['Song Kang-ho', 'Lee Sun-kyun', ..., 'Jang Hye-jin'], 'crew': ['Bong Joon-ho', 'Park Hyun-cheol', ..., 'Yoon Young-woo']}
    pprint(credits('검색할 수 없는 영화'))
    # None
