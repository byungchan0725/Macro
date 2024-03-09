import json
from urllib import request


def get_band_lists(token): # 내가 속해 있는 Band의 목록 확인 
    try:
        url = f'https://openapi.band.us/v2.1/bands?access_token={token}'
        req = request.Request(url)
        res = request.urlopen(req)
        decoded = res.read().decode("utf8")
        json_dict = json.loads(decoded)
        clean_bands = [{band['name']: band['band_key']} for band in json_dict['result_data']['bands']]
        # pprint(clean_bands)

        return clean_bands
    except:
        print("Access Token이 아닙니다.")
    # return clean_bands

def get_post_key(token, band_key): # 밴드 key를 가져옴 
    try:
        url = f'https://openapi.band.us/v2/band/posts?access_token={token}&band_key={band_key}&locale=ko_KR'
        req = request.Request(url)
        res = request.urlopen(req)
        decoded = res.read().decode("utf8")
        json_dict = json.loads(decoded)

        post_keys = [item['post_key'] for item in json_dict['result_data']['items']]
        print(post_keys)
        return post_keys

    except:
        print("올바른 band_key가 아닙니다.")
    