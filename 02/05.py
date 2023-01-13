import requests, os
from dotenv import load_dotenv
from pprint import pprint

def recommendation(title):
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

    res = list()

    if target:
        params = {'api_key': api_key, 'language': 'ko-KR'}
        temp = requests.get(url = url + f'movie/{target}/recommendations', params = params).json()
        
        for movie in temp['results']:
            res.append(movie['title'])
        return res
    else:
        return None

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화의 id를 기반으로 추천 영화 목록 구성
    추천 영화가 없을 경우 []를 반환
    영화 검색에 실패할 경우 None을 반환
    (주의) 추천 영화의 경우 아래 예시 출력과 차이가 있을 수 있음
    """
    pprint(recommendation('기생충'))
    # ['조커', '1917', '조조 래빗', ..생략.., '살인의 추억', '펄프 픽션']
    pprint(recommendation('그래비티'))
    # []
    pprint(recommendation('검색할 수 없는 영화'))
    # None
