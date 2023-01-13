import requests, os
from dotenv import load_dotenv
from pprint import pprint

def search_movie(title):
    load_dotenv()
    url = f'https://api.themoviedb.org/3/'
    api_key = os.getenv("tdmb_api")
    params = {'api_key': api_key, 'language': 'ko-KR', 'query': title, 'region': 'KR'}

    movieinfo = requests.get(url = url + 'search/movie', params = params).json()
    results = movieinfo['results']

    try:
        res = results[0]['id']
        return res
    except:
        return None

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화의 id 반환
    검색한 결과 영화가 없다면 None을 반환
    """
    print(search_movie('기생충'))
    # 496243
    print(search_movie('그래비티'))
    # 959101
    print(search_movie('검색할 수 없는 영화'))
    # None
