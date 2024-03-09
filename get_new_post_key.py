import json
from urllib import request

from create_comment import create_comment


def get_new_post_key(token, band_key):
    url = f'https://openapi.band.us/v2/band/posts?access_token={token}&band_key={band_key}&locale=ko_KR'
    req = request.Request(url)
    res = request.urlopen(req)
    decoded = res.read().decode("utf8")
    json_dict = json.loads(decoded)
    try:
        post_key = json_dict['result_data']['items'][0]['post_key']
        return post_key
    except (KeyError, IndexError):
        return None  # 최신 포스트 키를 찾지 못한 경우 None 반환

def checking_new_post(token, band_key, body):
    sw = True
    token = token 
    band_key = band_key
    temp = None 

    while sw:
        current_temp = get_new_post_key(token, band_key)
        if current_temp != temp and temp is not None:
            create_comment(token, band_key, current_temp, body)
            sw = False
            break 
        temp = current_temp

