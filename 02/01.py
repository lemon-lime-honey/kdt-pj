import requests, os
from dotenv import load_dotenv

def popular_count():
    load_dotenv()
    url = f'https://api.themoviedb.org/3/'
    api_key = os.getenv("tdmb_api")
    params = {'api_key': api_key, 'language': 'ko-KR', 'region': 'KR'}

    movieinfo = requests.get(url = url + 'movie/popular', params = params).json()
    results = movieinfo['results']
    res = len(results)

    return res

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count())
    # 20
